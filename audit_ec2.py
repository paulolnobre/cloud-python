instancias = [
    {"id": "i-001", "estado": "running",  "tipo": "t3.micro",  "nome": "web-server-1"},
    {"id": "i-002", "estado": "stopped",  "tipo": "t3.large",  "nome": "batch-processor"},
    {"id": "i-003", "estado": "running",  "tipo": "t3.large",  "nome": "api-gateway-proxy"},
    {"id": "i-004", "estado": "stopped",  "tipo": "t3.micro",  "nome": "dev-sandbox"},
    {"id": "i-005", "estado": "running",  "tipo": "t3.medium", "nome": "worker-node-1"},
    {"id": "i-006", "estado": "stopped",  "tipo": "t3.large",  "nome": "data-pipeline"},
]

ids_paradas = [i["id"] for i in instancias if i["estado"] == "stopped"]
t3_large_running = [i["id"] for i in instancias if i["estado"] == "running" and i["tipo"] == "t3.large"]

contagem = {}
for i in instancias:
    estado = i["estado"]
    contagem[estado] = contagem.get(estado, 0) + 1

print("=== EC2 Audit Report ===")
print(f"Instâncias paradas (candidatas a limpeza): {ids_paradas}")
print(f"Instâncias t3.large rodando (custo alto): {t3_large_running}")
print(f"Contagem por estado: {contagem}")