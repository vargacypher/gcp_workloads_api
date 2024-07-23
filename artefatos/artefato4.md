##### Artefato 4: Documentos de Políticas de Segurança, Controle de Acesso e Procedimentos de Auditoria

**1. Políticas de Segurança Implementadas:**

- **API gateway** : Para lidar com a autenticação e permissões dos usuarios ao recurso
- **Autorização Baseada em Papéis (RBAC):** Implemente o princípio do menor privilégio, atribuindo permissões mínimas necessárias para cada serviço.
- **Segregação de Funções:** Separado as responsabilidades entre diferentes serviços para evitar conflitos de interesse e reduzir riscos.


**2. Controle de Acesso:**

- **Autenticação:** A autenticação é realizada utilizando contas de serviço e chaves de serviço, garantindo a identidade dos serviços que acessam os recursos.

- **Autorização e Permissões Específicas aos servicos:** A autorização é realizada com base nas políticas IAM definidas para cada recurso, garantindo que apenas os usuários e serviços autorizados tenham acesso aos recursos.

**3. Procedimentos de Auditoria:**

- **Logs de Auditoria:** Habilitar logs dos serviços da GCP e utilizar o *Cloud Logging* para capturar e analisar logs de atividades e alterações.

- **Alertas de Segurança:** Configurar alertas para atividades suspeitas ou não autorizadas, utilizando o *Cloud Monitoring* para monitorar e configurar alertas baseados em métricas e logs.
