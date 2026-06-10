# Docker Deployment Guide

Complete setup para rodar o sistema Forex em containers Docker.

## O que é Docker?

Docker permite empacotar toda a aplicação (código, dependências, ambiente) em **containers** que rodam em qualquer lugar.

**Vantagens:**
- ✅ Sem problemas de "funciona na minha máquina"
- ✅ Deploy automático e rápido
- ✅ Fácil escalar (rodar múltiplas instâncias)
- ✅ Isolamento de componentes
- ✅ Consistência entre dev/staging/prod

---

## Architecture com Docker

```
┌─────────────────────────────────────────────────────────────┐
│                    Docker Network                           │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Frontend   │  │   Backend    │  │  PostgreSQL  │      │
│  │  Next.js:3000│  │ FastAPI:8000 │  │ Port:5432    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│         ↓                  ↓                  ↓              │
│  Port 3000           Port 8000          (internal)           │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐                        │
│  │    Redis     │  │    Nginx     │                        │
│  │ Port:6379    │  │  Port:80/443 │                        │
│  └──────────────┘  └──────────────┘                        │
│         ↓                  ↓                                │
│  (internal)          (external)                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Pré-requisitos

### Windows

1. **Docker Desktop for Windows**
   - Download: https://www.docker.com/products/docker-desktop
   - Requer Windows 10 Pro/Enterprise ou Windows 11

2. **Verificar instalação:**
   ```powershell
   docker --version
   docker-compose --version
   ```

3. **Ligar Docker Desktop**
   - Abra a aplicação "Docker Desktop"
   - Aguarde até estar pronto (ícone na bandeja)

### Linux

```bash
# Ubuntu/Debian
sudo apt-get install docker.io docker-compose

# Verificar
docker --version
docker-compose --version
```

### macOS

```bash
# Via Homebrew
brew install docker docker-compose

# Ou baixar Docker Desktop: https://www.docker.com/products/docker-desktop
```

---

## Setup Passo-a-Passo

### Step 1: Preparar ambiente

```bash
cd C:\Users\Matheus Lopes\Desktop\calopes-solucoes\forex

# Criar arquivo .env com suas credenciais
cp .env.example .env

# Editar .env com suas informações
# - OANDA_TOKEN
# - OANDA_ACCOUNT
# - DB_PASSWORD
```

**Arquivo .env:**
```env
OANDA_MODE=practice
OANDA_TOKEN=seu_token_aqui
OANDA_ACCOUNT=seu_account_aqui
DB_USER=forex
DB_PASSWORD=sua_senha_segura
ENVIRONMENT=development
```

### Step 2: Build das imagens

```bash
# Build de todas as imagens
docker-compose build

# Ou rebuild forçado
docker-compose build --no-cache
```

**Output esperado:**
```
Building backend
Building frontend
Building nginx
Successfully tagged forex-backend:latest
Successfully tagged forex-frontend:latest
```

### Step 3: Iniciar containers

```bash
# Iniciar tudo
docker-compose up -d

# Ver status
docker-compose ps

# Ver logs
docker-compose logs -f
```

**Output esperado:**
```
NAME              STATUS          PORTS
forex-backend     Up 2 minutes     0.0.0.0:8000->8000/tcp
forex-frontend    Up 2 minutes     0.0.0.0:3000->3000/tcp
forex-db          Up 2 minutes     0.0.0.0:5432->5432/tcp
forex-cache       Up 2 minutes     0.0.0.0:6379->6379/tcp
```

### Step 4: Acessar Dashboard

Abra no navegador: **http://localhost**

Ou acesso direto:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Database**: localhost:5432 (via pgAdmin)

---

## Comandos Docker Úteis

### Visualizar estado

```bash
# Status de todos os containers
docker-compose ps

# Logs do backend
docker-compose logs backend

# Logs do frontend
docker-compose logs frontend

# Logs em tempo real
docker-compose logs -f

# Últimas 100 linhas
docker-compose logs --tail=100
```

### Parar/Reiniciar

```bash
# Parar todos os containers
docker-compose stop

# Parar um container específico
docker-compose stop backend

# Reiniciar
docker-compose restart backend

# Parar e remover
docker-compose down

# Down com volumes (cuidado! deleta dados)
docker-compose down -v
```

### Executar comandos dentro de container

```bash
# Entrar no bash do backend
docker-compose exec backend bash

# Rodar Python command
docker-compose exec backend python -c "import pandas; print(pandas.__version__)"

# Rodar backtesting
docker-compose exec backend python run_all_strategies_backtest.py

# Entrar no psql (database)
docker-compose exec db psql -U forex -d forex
```

### Limpeza

```bash
# Remover containers inutilizados
docker system prune

# Remover tudo (containers, images, volumes)
docker system prune -a --volumes
```

---

## Troubleshooting Docker

### Erro: "Docker daemon not running"

**Solução Windows:**
- Abra "Docker Desktop" (ícone na bandeja)
- Aguarde até estar pronto

**Solução Linux:**
```bash
sudo systemctl start docker
```

### Erro: "Cannot bind port 3000"

**Causa:** Porta já está em uso

**Solução:**
```bash
# Ver qual processo está usando porta 3000
netstat -ano | findstr :3000

# Matar processo (Windows)
taskkill /PID [PID] /F

# Ou usar porta diferente no docker-compose.yml:
# ports:
#   - "3001:3000"
```

### Erro: "Cannot connect to Docker daemon"

**Solução Windows:**
- Docker Desktop não está rodando
- Inicie "Docker Desktop"

### Containers start mas ficam lento

**Causas possíveis:**
- Memória insuficiente
- Disco cheio
- Muitos containers rodando

**Solução:**
```bash
# Ver recursos dos containers
docker stats

# Aumentar recursos no Docker Desktop:
# Settings → Resources → Memory/CPUs
```

### Perda de dados ao fazer `docker-compose down -v`

**Aviso:** Isso deleta TODOS os volumes (banco de dados!)

**Solução:**
- Sempre fazer backup antes: `docker-compose exec db pg_dump -U forex forex > backup.sql`
- Usar `docker-compose down` sem `-v`

---

## Configuração de Produção

### 1. Usar PostgreSQL em vez de SQLite

No `docker-compose.yml`, já está pré-configurado. Para ativar:

```yaml
# backend environment:
DATABASE_URL=postgresql://forex:senha@db:5432/forex
```

### 2. Ativar HTTPS/SSL

1. Gere certificados:
```bash
# Self-signed (teste)
openssl req -x509 -newkey rsa:4096 -keyout certs/key.pem -out certs/cert.pem -days 365 -nodes

# Ou use Let's Encrypt (produção):
# https://letsencrypt.org/
```

2. Descomente seção HTTPS em `nginx.conf`

3. Reinicie Nginx:
```bash
docker-compose restart nginx
```

### 3. Variáveis de Ambiente Seguras

Use secrets do Docker (produção):

```bash
# Criar secret
echo "seu_token_super_secreto" | docker secret create oanda_token -

# No docker-compose:
# secrets:
#   oanda_token:
#     external: true
```

### 4. Monitoramento

```bash
# Ver CPU/memória em tempo real
docker stats

# Logs estruturados (ELK stack)
# Ver: https://www.elastic.co/docker
```

### 5. Backups Automáticos

```bash
# Script de backup diário
#!/bin/bash
docker-compose exec -T db pg_dump -U forex forex | gzip > backups/forex_$(date +%Y%m%d).sql.gz

# Adicione ao crontab:
# 0 2 * * * /path/to/backup.sh
```

---

## Performance Tips

### 1. Otimizar imagens

```bash
# Usar imagens mais leves (alpine)
# Já está no docker-compose.yml

# Multi-stage builds (frontend)
# Reduz tamanho final da imagem
```

### 2. Caching de layers

```dockerfile
# Dockerfile otimizado (backend):
FROM python:3.11-slim

WORKDIR /app

# Copy requirements primeiro (caching)
COPY requirements.txt .
RUN pip install -r requirements.txt  # Cache este layer

# Depois copy código
COPY . .
```

### 3. Usar volumes para desenvolvimento

```bash
# docker-compose.override.yml (desenvolvimento)
services:
  backend:
    volumes:
      - ./backend:/app
    environment:
      - RELOAD=true
```

---

## Deploy em Produção

### AWS EC2

```bash
# 1. SSH na instância
ssh -i key.pem ec2-user@your-instance

# 2. Instalar Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# 3. Clonar repositório
git clone your-repo
cd forex

# 4. Setup .env com vars de produção
cp .env.example .env
nano .env

# 5. Iniciar
docker-compose up -d
```

### Heroku

```bash
# 1. Instalar Heroku CLI
# 2. Login
heroku login

# 3. Criar app
heroku create forex-trading

# 4. Deploy
git push heroku main

# 5. Ver logs
heroku logs --tail
```

### DigitalOcean App Platform

1. Push código para GitHub
2. Conecte repo no DigitalOcean
3. Configure `docker-compose.yml`
4. Deploy automático

---

## Monitorar em Produção

### Health Checks

Já configurados em `docker-compose.yml`:

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
  interval: 30s
  timeout: 10s
  retries: 3
```

### Logs Centralizados

```bash
# Ver logs com timestamps
docker-compose logs --timestamps

# Exportar para arquivo
docker-compose logs > logs.txt

# Usar ELK Stack (recomendado em produção)
```

### Alertas

Configure alerts via:
- **Prometheus** + **AlertManager**
- **Datadog**
- **New Relic**

---

## Checklist de Deploy

- [ ] Docker Desktop instalado e rodando
- [ ] Docker-compose v2+
- [ ] Arquivo .env criado com credenciais
- [ ] `docker-compose build` sem erros
- [ ] `docker-compose up -d` iniciando containers
- [ ] `docker-compose ps` mostrando todos UP
- [ ] Frontend acessível em http://localhost:3000
- [ ] Backend acessível em http://localhost:8000
- [ ] API /health respondendo
- [ ] Database conectado
- [ ] Redis rodando
- [ ] Logs sem errors críticos

---

## Próximas Steps

1. ✅ Docker setup completo
2. ⏳ Rodar backtesting (`docker-compose exec backend python run_all_strategies_backtest.py`)
3. ⏳ Paper trading em sandbox OANDA
4. ⏳ Go live com pequeno capital

---

## Suporte

### Problemas comuns

**Backend não inicia:**
```bash
docker-compose logs backend
```

**Frontend em branco:**
```bash
docker-compose logs frontend
```

**Database connection refused:**
```bash
docker-compose logs db
docker-compose exec db psql -U forex -d forex -c "SELECT 1"
```

**Performance lenta:**
```bash
docker stats
# Se CPU/MEM alta, aumentar em Docker Desktop Settings
```

---

## Leitura Adicional

- Docker Docs: https://docs.docker.com/
- Docker Compose: https://docs.docker.com/compose/
- Best Practices: https://docs.docker.com/develop/dev-best-practices/
