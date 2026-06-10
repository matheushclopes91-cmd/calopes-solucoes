.PHONY: help build start stop restart logs health clean clean-all backtest db-backup db-restore

# Colors
RED := \033[0;31m
GREEN := \033[0;32m
YELLOW := \033[1;33m
NC := \033[0m

help:
	@echo "$(GREEN)Forex Trading System - Docker Management$(NC)"
	@echo ""
	@echo "Usage: make [command]"
	@echo ""
	@echo "$(YELLOW)Build & Start:$(NC)"
	@echo "  make build          Build Docker images"
	@echo "  make start          Start all containers"
	@echo "  make stop           Stop all containers"
	@echo "  make restart        Restart all containers"
	@echo ""
	@echo "$(YELLOW)Monitoring:$(NC)"
	@echo "  make logs           View all container logs"
	@echo "  make logs-backend   View backend logs only"
	@echo "  make logs-frontend  View frontend logs only"
	@echo "  make status         Show containers status"
	@echo "  make health         Check service health"
	@echo ""
	@echo "$(YELLOW)Development:$(NC)"
	@echo "  make shell-backend  Enter backend container"
	@echo "  make shell-frontend Enter frontend container"
	@echo "  make shell-db       Enter database container"
	@echo ""
	@echo "$(YELLOW)Trading:$(NC)"
	@echo "  make backtest       Run strategy backtest"
	@echo "  make test-api       Test API endpoints"
	@echo ""
	@echo "$(YELLOW)Database:$(NC)"
	@echo "  make db-backup      Backup database"
	@echo "  make db-restore     Restore database from backup"
	@echo ""
	@echo "$(YELLOW)Cleanup:$(NC)"
	@echo "  make clean          Stop and remove containers"
	@echo "  make clean-all      Remove everything (WARNING: deletes data!)"
	@echo ""

build:
	@echo "$(YELLOW)Building Docker images...$(NC)"
	docker-compose build
	@echo "$(GREEN)✓ Build complete$(NC)"

start:
	@echo "$(YELLOW)Starting containers...$(NC)"
	docker-compose up -d
	@sleep 3
	@echo "$(GREEN)✓ Containers started$(NC)"
	@$(MAKE) status

stop:
	@echo "$(YELLOW)Stopping containers...$(NC)"
	docker-compose stop
	@echo "$(GREEN)✓ Containers stopped$(NC)"

restart: stop start

logs:
	docker-compose logs -f

logs-backend:
	docker-compose logs -f backend

logs-frontend:
	docker-compose logs -f frontend

logs-db:
	docker-compose logs -f db

status:
	@echo "$(YELLOW)Container Status:$(NC)"
	@docker-compose ps

health:
	@echo "$(YELLOW)Checking service health...$(NC)"
	@if docker-compose exec -T backend curl -f http://localhost:8000/health 2>/dev/null; then \
		echo "$(GREEN)✓ Backend is healthy$(NC)"; \
	else \
		echo "$(RED)✗ Backend is not responding$(NC)"; \
	fi
	@if docker-compose exec -T db psql -U forex -d forex -c "SELECT 1" 2>/dev/null; then \
		echo "$(GREEN)✓ Database is healthy$(NC)"; \
	else \
		echo "$(RED)✗ Database is not responding$(NC)"; \
	fi

shell-backend:
	docker-compose exec backend bash

shell-frontend:
	docker-compose exec frontend bash

shell-db:
	docker-compose exec db psql -U forex -d forex

backtest:
	@echo "$(YELLOW)Running strategy backtest...$(NC)"
	docker-compose exec backend python run_all_strategies_backtest.py

test-api:
	@echo "$(YELLOW)Testing API endpoints...$(NC)"
	@curl -s http://localhost:8000/docs && echo "$(GREEN)✓ API is responding$(NC)" || echo "$(RED)✗ API is not responding$(NC)"

db-backup:
	@echo "$(YELLOW)Backing up database...$(NC)"
	@mkdir -p backups
	@docker-compose exec -T db pg_dump -U forex forex | gzip > backups/forex_$$(date +%Y%m%d_%H%M%S).sql.gz
	@echo "$(GREEN)✓ Backup complete$(NC)"

db-restore:
	@if [ -z "$(FILE)" ]; then \
		echo "$(RED)✗ Usage: make db-restore FILE=backups/forex_*.sql.gz$(NC)"; \
		exit 1; \
	fi
	@echo "$(YELLOW)Restoring database from $(FILE)...$(NC)"
	@gunzip < $(FILE) | docker-compose exec -T db psql -U forex -d forex
	@echo "$(GREEN)✓ Restore complete$(NC)"

clean:
	@echo "$(YELLOW)Cleaning up Docker resources...$(NC)"
	docker-compose down
	@echo "$(GREEN)✓ Cleanup complete$(NC)"

clean-all:
	@echo "$(RED)WARNING: This will delete all containers, images, and data!$(NC)"
	@read -p "Are you sure? (y/n) " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		echo "$(YELLOW)Removing all Docker resources...$(NC)"; \
		docker-compose down -v; \
		docker system prune -a --volumes -f; \
		echo "$(GREEN)✓ Full cleanup complete$(NC)"; \
	else \
		echo "$(YELLOW)Cleanup cancelled$(NC)"; \
	fi

# Development helpers
dev-logs:
	@$(MAKE) logs

dev-shell:
	@$(MAKE) shell-backend

dev-test:
	@$(MAKE) test-api

# Production helpers
prod-build:
	@echo "$(YELLOW)Building production images...$(NC)"
	docker-compose -f docker-compose.yml build
	@echo "$(GREEN)✓ Production build complete$(NC)"

prod-start:
	@echo "$(YELLOW)Starting production containers...$(NC)"
	docker-compose up -d
	@echo "$(GREEN)✓ Production containers started$(NC)"
	@$(MAKE) health

prod-deploy: clean build prod-start
	@echo "$(GREEN)✓ Production deployment complete$(NC)"

# Useful aliases
up: start
down: stop
ps: status
