FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    git \
    curl \
    wget \
    tree \
    htop \
    build-essential \
    ca-certificates \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Instalar OpenCode
RUN curl -fsSL https://opencode.ai/install | bash \
    && /root/.opencode/bin/opencode --version

ENV PATH="/root/.opencode/bin:${PATH}"

# Requirements.txt
COPY ./.devcontainer/requirements.txt .

RUN python -m pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

CMD ["bash"]
