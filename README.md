#  FastAPI Users API

CRUD de usuarios utilizando **FastAPI**, **MySQL** y **SQLAlchemy**, con validación de datos mediante **Pydantic**. El proyecto está estructurado siguiendo buenas prácticas para producción.

---

## 🚀 Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [MySQL](https://www.mysql.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

## 🧱 Estructura del proyecto

```
├── app/
│ ├── main.py
│ ├── api/
│ │ └── routes_user.py
│ ├── crud/
│ │ └── user.py
│ ├── models/
│ │ └── user.py
│ ├── schemas/
│ │ └── user.py
│ ├── database/
│ │ └── session.py
│ └── core/
│ └── config.py
├── .env
├── requirements.txt
├── db_users.sql
└── README.md
```

## 🧪 Endpoints principales
### ✅ `/proyectos`
Devuelve la lista de proyectos para mostrar en el frontend del portafolio.

- **Método:** `GET`
- **Respuesta:** JSON con la información de los proyectos.

### ✅ `/contacto`
Recibe el formulario de contacto y envía un correo con los datos.

- **Método:** `POST`
- **Body:** JSON con los campos: `nombre`, `telefono`, `email`, `asunto`, `mensaje`
- **Validaciones:** implementadas con `Pydantic`
- **Envío:** mediante `FastAPI-Mail` usando variables de entorno

---

##  Crear el entorno virtual

```bash
python -m venv venv
# Activar entorno en Windows:
.\venv\Scripts\Activate.ps1
# O en CMD:
venv\Scripts\activate
```

## ⚙️ Requisitos previos
- Python 3.10+
- MySQL instalado localmente (ej. MySQL Workbench)

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/fastapi-users-api.git
cd tu-repo
```
### 2.  Instalar dependencias
```bash
pip install -r requirements.txt
```
### 3. Crear la base de datos en MySQL
Abrí MySQL Workbench o terminal y ejecuta 
```bash
mysql -u root -p < db_users.sql
```

### 4.  Crear el archivo .env
```bash
DB_URL=mysql+pymysql://usuario:contraseña@localhost/tubasededatos
```
### 5.  Ejecutar el servidor
```bash
uvicorn main:app --reload
```
