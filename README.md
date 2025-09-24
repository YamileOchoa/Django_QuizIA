# 📝 QuizzIA

QuizzIA es una aplicación de cuestionarios interactivos desarrollada como parte de la guía del curso.  
Este proyecto utiliza **Django** para el backend y **Node.js** para la gestión de dependencias/front-end.

---

## 🔧 Requisitos previos

Antes de comenzar, asegúrate de tener instalado en tu sistema:

- **Python 3.x**
- **Django** (última versión estable)
- **pip** (administrador de paquetes de Python)
- **Entorno virtual (venv)** para aislar dependencias
- **Node.js** (con npm o yarn)

---

## 🐍 Versión de Python

Para confirmar la versión de **Python** instalada en el sistema, ejecuta en la terminal:

```bash
python --version
```

---

## 🌐 Versión de Node.js

Para confirmar la versión de **Node.js** instalada en el sistema:

```bash
node --version
```

Para confirmar la versión de **npm** (administrador de paquetes de Node.js):

```bash
npm --version
```

---

## 📂 Crear proyecto en Django

Primero crea una carpeta para tu proyecto:

```bash
mkdir Django_QuizzIA
cd Django_QuizzIA
```

---

## 🛠️ Crear y activar entorno virtual

Crea un entorno virtual con:

```bash
python -m venv venv
```

Activa el entorno virtual:

**En Windows:**

```bash
venv\Scripts\activate
```

**En Linux / MacOS:**

```bash
source venv/bin/activate
```

---

## ⚙️ Instalar Django

Con el entorno virtual activado, instala Django:

```bash
pip install django
```

---

## 🚀 Crear proyecto base

Crea el proyecto principal de Django llamado QuizzIA:

```bash
django-admin startproject QuizzIA
```

Entra a la carpeta del proyecto:

```bash
cd QuizzIA
```

Ejecuta el servidor para verificar que todo funciona:

```bash
python manage.py runserver
```
