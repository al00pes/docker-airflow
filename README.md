Docker Airflow - Projeto de Orquestração de Dados
Este repositório contém a estrutura para deploy do Apache Airflow utilizando Docker, com foco na orquestração de pipelines de dados, ingestão em armazenamento em nuvem e disponibilização para visualização no Power BI.

🚀 Tecnologias utilizadas
Apache Airflow

Docker / Docker Compose

Python

Azure Blob Storage (ou outro serviço de armazenamento em nuvem)

Power BI

📄 Descrição do Projeto
A automação é responsável por:

Realizar a extração de relatórios de diferentes fontes.

Orquestrar o envio dos dados para a nuvem (storage).

Atualizar bases de dados para consumo posterior no Power BI.

Garantir a execução monitorada e organizada das tarefas via Airflow (DAGs).

O projeto é ideal para quem deseja criar um pipeline de dados robusto e escalável utilizando Airflow em ambiente Dockerizado.

🛠️ Como executar o projeto
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/al00pes/docker-airflow.git
cd docker-airflow
Suba os containers com Docker Compose:

bash
Copiar
Editar
docker-compose up -d
Acesse o Airflow WebServer:

URL: http://localhost:8080

Login padrão:

Username: airflow

Password: airflow

Configurar suas DAGs:

As DAGs estão localizadas na pasta /dags.

Customize conforme seu fluxo de dados e suas necessidades.

Observação:

Verifique as credenciais e configurações para conexão com a nuvem no seu arquivo de variáveis/conexões do Airflow.

📁 Estrutura de Pastas
bash
Copiar
Editar
docker-airflow/
├── dags/           # DAGs personalizadas
├── docker-compose.yml
├── airflow.cfg     # (Se aplicável, configurações adicionais)
├── requirements.txt
└── README.md
✨ Melhorias Futuras
Implementação de monitoramento com alertas via e-mail ou WhatsApp.

Integração com mais provedores de cloud storage.

Templates prontos para ingestão de dados de APIs públicas.

📢 Contato
Em caso de dúvidas, sugestões ou contribuições, fique à vontade para entrar em contato!

Seu LinkedIn

[Seu E-mail] (opcional)

🐳 Observação importante
Este projeto utiliza imagens oficiais do Airflow mantidas pela Apache Foundation, e foi adaptado para facilitar o desenvolvimento local e pequenos ambientes de produção/teste.
