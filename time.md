
# ===== Resumen de actividad =====

📅 2025-01-27: 5 horas
   🔹 Commits del día:
      - Refactor TareaResponsableRequest class in tarea_responsable.py to inherit from BaseModel instead of PaginationRequest for improved clarity and functionality
      - Remove unused route imports from api_router.py for improved clarity and maintainability
      - Remove commented-out code from auth.py and common_controller.py for improved code clarity
      - Refactor server.py to improve application structure and add detailed startup logging; enhance middleware and router initialization
      - Add IDs to NotificationResponse and correct typo in TareaResponsableResponse for improved data accuracy
      - Remove transactional.py as it is no longer needed for database operations
      - Add DBContext class for database operations and remove unused code from dashboard_controller.py
      - Rename FastApiFunction to ApiServerlessFunction in infrastructure.yaml for improved clarity
      - Remove unused service files related to dashboard notifications and responsables for codebase cleanup
      - Refactor dashboard_controller.py to use DBContext for database operations and remove unused fetch functions for improved clarity and maintainability
      - Refactor getDonutPanel function in dashboard_controller.py to remove commented-out code and simplify data fetching logic for improved readability
      - Add AWS SAM template for FastAPI deployment with initial function configuration
      - Remove commented-out PaginationRequest class from notificaciones.py and tarea_responsable.py for improved code clarity

📅 2025-01-15: 2 horas
   🔹 Commits del día:
      - Refactor stored procedures to use a list structure for improved readability and error handling during execution
      - Refactor stored procedures for improved data types and add drop_procedures method; update server and service files accordingly

📅 2025-01-14: 4 horas
   🔹 Commits del día:
      - Add fetch_notificaciones service and corresponding database function; update dashboard controller to utilize new service
      - Refactor GetResponsable endpoint to use stored procedure for fetching responsables; update response handling and logging
      - Implement fetch_requirement_obligation service and update dashboard controller; modify response model fields for consistency
      - Add fetch_donut_panel service and corresponding database function; update dashboard controller to utilize new service
      - Rename variable for stored procedures in database module for clarity
      - Add fetch_total_solicitudes_revisor service and corresponding database function; update dashboard controller to utilize new service
      - Add fetch_expediente_civa service and corresponding database function; update dashboard controller to utilize new service
      - Add fetch_tareas_responsable service and corresponding database function; update dashboard controller to utilize new service

📅 2025-01-09: 6 horas
   🔹 Commits del día:
      - Add AreaRolModel and ResponsableModel, and update imports in schemas
      - Add DatosempresaEvidenciaIDRequest model and update getEvidenciaID endpoint
      - Add empty response model files for requirements
      - Add request models for ProveedorNacional and CaracterTipos, and update response schemas
      - Add request and response models for dashboard features including TotalSolicitudesRevisor, Notificaciones, ExpedienteCiva, RequerimientoObligaciones, DonutPanel, and TareaResponsable
      - Add request models for RazonSocial and DatosEmpresa endpoints and log requests
      - Update getSectionList endpoint to use SectionDatosEmpresaListRequest and add new request schema
      - Add SectionOptionDatosEmpresaResponse model and update getSectionList endpoint
      - Move response models for ExpedienteCiva and RequirementObligations to a new response module
      - Refactor response handling to replace PaginationBase with ListResponse in company data and requirements controllers
      - Add request and response models for LegalUso and EnlaceOperativo, and update related endpoints
      - Add request models for dashboard features including DonutPanel, ExpedienteCiva, Notificaciones, RequerimientoObligaciones, TareaResponsable, and TotalSolicitudesRevisor
      - Add request and response models for requerimientos, including section options and hallazgos
      - Add empty request model files for hallazgo and requerimientos
      - Add request models for SocioAccionista and LegalUso, and update related endpoints
      - Remove obsolete response models for ExpedienteCiva and RequirementObligations, and add new ExpedienteCivaResponse model
      - Update response handling and refactor model imports in company data schemas; modify login response structure and adjust excluded URLs in config
      - Add request and response models for countries and states, and update schema imports
      - Add initial model imports in __init__.py for schema organization
      - Add DatosEmpresaEnlaceOperativoModel and update related imports in schemas

📅 2025-01-08: 2 horas
   🔹 Commits del día:
      - Refactor API response and request schemas for consistency and clarity
      - Chat GPT refactor
      - Refactor Chat GPT
      - Refactor GetResponsable function to simplify data handling and improve readability
      - Refactor company_data_controller to reorganize import statements for improved clarity
      - Chat GPT refactor 3

📅 2025-01-07: 5 horas
   🔹 Commits del día:
      - Rename API endpoints for consistency and clarity
      - Update ROUTE_PATH in configuration from '/app/v1' to '/api'
      - Update import path for Base model and comment out database seeding in server startup
      - Rename endpoint from '/get_responsable' to '/GetResponsable' for consistency
      - Rename login endpoint for consistency and clarity
      - Refactor company data API endpoints for consistency and clarity
      - Rename dashboard API endpoints for consistency and clarity

📅 2025-01-06: 3 horas
   🔹 Commits del día:
      - Refactor responsable schemas by consolidating request and response models into common files
      - Refactor requirements response schemas by removing obsolete file and consolidating response model
      - Add State and Client models to database initialization
      - Add black formatter to development requirements
      - Refactor dashboard schemas by consolidating response models and removing obsolete date request schema
      - Remove obsolete RequerementsObligationsResponse import from company_data_controller and requirements_controller
      - Remove obsolete requirements response schema
      - Black Formatter aplied
      - Refactor authentication schemas by consolidating request and response models into single files
      - Refactor responsable schemas by consolidating request and response models into single files

📅 2025-01-05: 4 horas
   🔹 Commits del día:
      - Update requirements controller endpoints to enhance request and response schemas
      - Refactor database models to enhance relationships and update schemas for clients, states, and notifications
      - Add company data controller to API router
      - Update getSolicitudID endpoint to enhance request and response schemas
      - Refactor dashboard controller endpoints to update request and response schemas for obligations, notifications, and tasks
      - Update company data controller endpoints to enhance request and response schemas
      - Refactor company data controller endpoints to update request and response schemas for legal use and related data
      - Add requirements controller to API router

📅 2025-01-03: 3 horas
   🔹 Commits del día:
      - Remove ResponseLogMiddleware and related classes to streamline middleware functionality
      - Add dashboard controller and implement requirements obligations endpoint with response schema
      - Refactor dashboard controller endpoints and add new functionality for obligations, notifications, and tasks
      - Add logging for error handling in GetResponsable and GetRequirementObligation endpoints
      - Add GetResponsable endpoint with pagination and response schema for fetching responsables
      - Refactor common_controller routes and update GetResponsable endpoint for improved error handling and response structure
      - Update documentation for GetResponsable endpoint to clarify request parameters
      - Remove user-related routes and schemas from the API, simplifying the router configuration

📅 2025-01-02: 5 horas
   🔹 Commits del día:
      - Add database seeding functionality: implement seed_database method to populate roles in the database during startup.
      - Remove SQLAlchemy middleware and related session management: delete SQLAlchemyMiddleware and its references to streamline middleware components.
      - Add database backup instructions to README: include steps for creating and copying database backups using Docker
      - Add excluded URLs to LocalConfig for API access control
      - Enhance logging in database population and server initialization: prefix log messages with context identifiers for better traceability.
      - Add GetResponsable endpoint to retrieve responsables with role-based access control

📅 2025-01-01: 1 hora
   🔹 Commits del día:
      - Add database models and table creation logic: implement models for countries, findings, responsables, and others; include async table creation in the database population script.

📅 2024-12-30: 3 horas
   🔹 Commits del día:
      - Refactor database session management: streamline session handling with async session factory and update JWT configuration structure in config files
      - Add PostgreSQL Docker setup and initialization scripts
      - Update database configuration and add ORM models: restructure config.json for multiple databases and implement SQLAlchemy models for users, roles, tasks, and more.
      - Update database configuration to use PostgreSQL: modify connection strings and update config settings for one-core database

📅 2024-12-22: 3 horas
   🔹 Commits del día:
      - Add Python version file: specify Python version 3.10.11
      - Refactor configuration management: load production settings from JSON file and update default values
      - Move folders
      - Refactor configuration management: replace old config.json with updated version and adjust ROUTE_PATH format
      - Refactor logger configuration: move logger_config to config directory and update import paths
      - Refactor routing configuration: update ROUTE_PATH and clean up unused imports
      - Update requirements management: rename requirements file and regenerate requirements.txt
      - Add development requirements file: create dev-requirements.txt and include necessary packages
      - Refactor service structure: move auth and role_checker services to a new directory and update import paths

📅 2024-12-18: 5 horas
   🔹 Commits del día:
      - Add user management routes and update authentication response structure
      - Refactor logger configuration: comment out existing logging setup and initialize logger for 'uvicorn.error'
      - Refactor Create function: rename dependency parameter for clarity
      - Refactor authentication logic: update token payload structure, enhance token generation with expiration, and modify user data handling
      - Refactor configuration management: load environment variables for app settings and update default values
      - Black Format
      - Implement logging for authentication middleware and application startup

📅 2024-12-17: 1 hora
   🔹 Commits del día:
      - Refactor authentication schemas and responses: update field names to PascalCase and enhance ApiResponse structure
      - Refactor authentication module: rename token request/response schemas, implement login endpoint, and add JWT token creation logic

📅 2024-12-16: 1 hora
   🔹 Commits del día:
      - Refactor authentication middleware and routes: update token verification logic and improve security handling

📅 2024-12-14: 6 horas
   🔹 Commits del día:
      - Update README to reflect changes in virtual environment setup and main script execution
      - first commit
      - Implement authentication and response logging middleware; update requirements
      - Add configuration management and main application entry point
      - Refactor API router and schemas: remove old files and add updated implementations
      - Add .gitignore file to exclude common Python artifacts and environment files
      - Refactor authentication routes and middleware: update response handling and add verification endpoint
      - Refactor configuration settings and add initial FastAPI application structure
      - Add SQLAlchemy session management and transactional middleware; update requirements
      - Add API router and include login routes
      - Refactor API structure: remove old router, add new auth routes and schemas

⏳ Tiempo total trabajado: 56 horas

# ===== Reuniones de equipo =====

📅 Total 6 horas

# ===== TOTAL GENERAL =====

⏳ Tiempo total trabajado: 62 horas