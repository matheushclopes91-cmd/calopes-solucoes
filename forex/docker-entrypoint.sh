#!/bin/bash

# Docker entrypoint script for forex system
# Usage: ./docker-entrypoint.sh [command]

set -e

DOCKER_COMPOSE="docker-compose"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Helper functions
print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_info() {
    echo -e "${YELLOW}ℹ${NC} $1"
}

# Check if Docker is running
check_docker() {
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed"
        exit 1
    fi

    if ! docker info &> /dev/null; then
        print_error "Docker daemon is not running. Please start Docker."
        exit 1
    fi

    print_status "Docker is running"
}

# Check if .env exists
check_env() {
    if [ ! -f ".env" ]; then
        print_error ".env file not found"
        print_info "Creating .env from .env.example..."
        cp .env.example .env
        print_info "Please edit .env with your credentials"
        exit 1
    fi
    print_status ".env file found"
}

# Build images
build() {
    print_info "Building Docker images..."
    $DOCKER_COMPOSE build
    print_status "Build complete"
}

# Start containers
start() {
    print_info "Starting containers..."
    $DOCKER_COMPOSE up -d
    print_status "Containers started"

    # Wait for services to be ready
    print_info "Waiting for services to be ready..."
    sleep 5

    print_info "Service status:"
    $DOCKER_COMPOSE ps
}

# Stop containers
stop() {
    print_info "Stopping containers..."
    $DOCKER_COMPOSE stop
    print_status "Containers stopped"
}

# View logs
logs() {
    if [ -z "$1" ]; then
        $DOCKER_COMPOSE logs -f
    else
        $DOCKER_COMPOSE logs -f $1
    fi
}

# Execute command in container
exec_cmd() {
    local service=$1
    shift
    $DOCKER_COMPOSE exec $service "$@"
}

# Health check
health() {
    print_info "Checking health..."

    # Check backend
    if $DOCKER_COMPOSE exec -T backend curl -f http://localhost:8000/health &> /dev/null; then
        print_status "Backend is healthy"
    else
        print_error "Backend is not responding"
    fi

    # Check database
    if $DOCKER_COMPOSE exec -T db psql -U forex -d forex -c "SELECT 1" &> /dev/null; then
        print_status "Database is healthy"
    else
        print_error "Database is not responding"
    fi

    # Check frontend
    if $DOCKER_COMPOSE exec -T frontend curl -f http://localhost:3000 &> /dev/null; then
        print_status "Frontend is healthy"
    else
        print_error "Frontend is not responding"
    fi
}

# Run backtest
backtest() {
    print_info "Running backtest..."
    $DOCKER_COMPOSE exec backend python run_all_strategies_backtest.py
}

# Database operations
db_backup() {
    local filename="backups/forex_$(date +%Y%m%d_%H%M%S).sql.gz"
    print_info "Backing up database to $filename..."
    mkdir -p backups
    $DOCKER_COMPOSE exec -T db pg_dump -U forex forex | gzip > $filename
    print_status "Backup complete: $filename"
}

db_restore() {
    if [ -z "$1" ]; then
        print_error "Usage: $0 db-restore <backup.sql.gz>"
        exit 1
    fi

    print_info "Restoring database from $1..."
    gunzip < $1 | $DOCKER_COMPOSE exec -T db psql -U forex -d forex
    print_status "Restore complete"
}

# Cleanup
clean() {
    print_info "Cleaning up Docker resources..."
    $DOCKER_COMPOSE down
    print_status "Cleanup complete"
}

clean_all() {
    print_info "Removing all containers, images, and volumes..."
    $DOCKER_COMPOSE down -v
    docker system prune -a --volumes
    print_status "Full cleanup complete"
}

# Display usage
usage() {
    cat << EOF
${GREEN}Forex Trading System - Docker Control Script${NC}

Usage: $0 [command] [options]

Commands:
    build               Build Docker images
    start               Start all containers
    stop                Stop all containers
    restart             Restart all containers
    logs [service]      View container logs
    status              Show containers status
    health              Check service health
    exec [service]      Execute command in container

    backtest            Run strategy backtest

    db-backup           Backup database
    db-restore <file>   Restore database from backup

    clean               Stop and remove containers
    clean-all           Remove everything (WARNING: deletes data!)

    help                Show this help message

Examples:
    $0 start                    # Start all services
    $0 logs backend             # View backend logs
    $0 exec backend bash        # Enter backend container
    $0 backtest                 # Run backtest
    $0 db-backup                # Backup database

${YELLOW}Note:${NC} Make sure Docker is running and .env is configured before running commands.

EOF
}

# Main script
main() {
    check_docker
    check_env

    if [ -z "$1" ]; then
        usage
        exit 0
    fi

    case "$1" in
        build)
            build
            ;;
        start)
            start
            ;;
        stop)
            stop
            ;;
        restart)
            stop
            start
            ;;
        logs)
            logs $2
            ;;
        status)
            $DOCKER_COMPOSE ps
            ;;
        health)
            health
            ;;
        exec)
            shift
            exec_cmd "$@"
            ;;
        backtest)
            backtest
            ;;
        db-backup)
            db_backup
            ;;
        db-restore)
            db_restore $2
            ;;
        clean)
            clean
            ;;
        clean-all)
            read -p "Are you sure? This will delete all data! (y/n) " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                clean_all
            else
                print_info "Cleanup cancelled"
            fi
            ;;
        help)
            usage
            ;;
        *)
            print_error "Unknown command: $1"
            usage
            exit 1
            ;;
    esac
}

main "$@"
