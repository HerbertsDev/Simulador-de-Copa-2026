# Simulador de Copa do Mundo 2026

## Como executar
1. Tenha Python 3 instalado
2. Execute: `python copa.py`

## O que o programa faz
- Simula as fases eliminatórias da Copa 2026 (oitavas, quartas, semi e final)
- Sorteia os placares aleatoriamente
- Resolve empates nos pênaltis
- Salva todos os resultados num banco de dados SQLite

## Exemplo de saída

Oitavas de Final: Brasil 2 x 1 México → Passa: Brasil
...
🏆 Campeão da Copa 2026: Alemanha

## Arquivos
- `copa.py` — código principal
- `consultas.sql` — scripts SQL para consultar os dados
- `copa2026.db` — banco de dados gerado ao rodar
