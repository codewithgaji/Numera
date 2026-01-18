# 🚀 Deploying a Django Application on AWS EC2 with Apache & WSGI

Ehhhh, let me explain how I deployed my first Django application on an AWS EC2 instance using **Apache + mod_wsgi**, including the challenges I faced, discoveries I made, and how I solved them with the help of AI.

---

## 📌 Overview

Initially, I attempted to deploy my application like a normal static website using Apache. But then I realized that the project i was setting up was a **Django application**, which requires a Python execution layer. This led me to learn and configure **WSGI**, the bridge between Apache and Django.

What I'm about to explain covers:
- AWS CLI setup and authentication
- EC2 instance provisioning
- Fast cloud-based installations
- Apache setup
- Understanding why `index.html` was not rendering
- Django + Apache integration using WSGI
- Static files handling
- Final working architecture

---

## 🧰 AWS CLI Setup & Authentication

To interact with AWS from my terminal, I installed and configured the AWS CLI.

### 1️⃣ Install AWS CLI

```bash
sudo apt update
sudo apt install awscli -y
```

### 2️⃣ Configure AWS CLI

```bash
aws configure
```

I provided:
- **AWS Access Key ID**
- **AWS Secret Access Key**
- **Default region** (e.g. `us-east-1`)
- **Output format** (`json`)

This links my local terminal directly to my AWS account, allowing me to manage resources from the command line.

---

## ☁️ Launching the EC2 Instance

### Instance Details

- **Name:** Web03
- **AMI:** Ubuntu Linux (`ami-0ecb62995f68g3begdd9`) Not sure if this should be shown here, lol
- **Instance Type:** `t3.micro`
- **Security Group:** `mysg`
- **Key Pair:** selected during launch (critical for SSH)

### First Discovery 💡

**Cloud server installations are extremely fast.**
Trust me, i did not see this coming 😂

Because EC2 instances pull packages directly from optimized cloud mirrors, commands like `apt install` run much faster than on local machines.

---

## 🛠 Initial Server Setup

After SSH-ing into the instance:
Not sure if it is "sshing" so just left it with an iphen(is this spelt correctly?)
```bash
apt update
apt install apache2 wget unzip vim -y
```

Apache was installed and running successfully.

---

## 📦 Pulling Project from GitHub

```bash
wget https://github.com/codewithgaji/Numera/archive/refs/heads/master.zip
unzip master.zip
```

GitHub extracts repositories into a folder named:
```
Numera-master
```

So this created:
```
Numera-master/
```

I copied the contents into Apache's web root:

```bash
cp -r Numera-master/* /var/www/html/
```

---

## ❌ The Problem: Apache Default Page Still Showing

Even though `index.html` existed, Apache kept showing:
```
Apache2 Ubuntu Default Page
```

Running:
```bash
ls /var/www/html
```

revealed this:
```
manage.py
converter/
numera/
templates/
staticfiles/
index.html
```

At this point, I realized something important.

---

## 🔍 Critical Discovery: This Is a Django Project, lol

My actual page was located at:
```
converter/templates/index.html
```

**This is not a static HTML file.**

### Why this matters:

- Apache can only serve **static files**
- Django templates require **Python execution**
- Templates are rendered by `views.py`, not Apache
- So simply "linking Apache" to the file would never work.

---

## 🧠 Understanding WSGI (Key Concept)

**WSGI (Web Server Gateway Interface)** is the bridge between:

```
Browser → Apache → WSGI → Django → Python → Response
```

- **Apache** handles HTTP
- **Django** runs Python logic
- **WSGI** translates HTTP requests into Python calls

**Without WSGI, Apache cannot run Django.**

---

## ⚙️ Installing WSGI & Python Environment - I used AI to explain this part of my doc.

```bash
apt install python3-venv python3-pip libapache2-mod-wsgi-py3 -y
```

Verified:

```bash
apache2ctl -M | grep wsgi
```

✅ Output: `wsgi_module (shared)`

---

## 🧪 Virtual Environment Setup

```bash
cd /var/www/html
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py check
```

Django system check passed (static warning ignored for now).

---

## 🌐 Configuring Apache to Serve Django

### Create Apache Site Config

```bash
sudo nano /etc/apache2/sites-available/numera.conf
```

Add the following configuration:

```apache
<VirtualHost *:80>
    ServerName _

    Alias /static /var/www/html/staticfiles
    <Directory /var/www/html/staticfiles>
        Require all granted
    </Directory>

    <Directory /var/www/html/numera>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess numera python-home=/var/www/html/venv python-path=/var/www/html
    WSGIProcessGroup numera
    WSGIScriptAlias / /var/www/html/numera/wsgi.py

    ErrorLog ${APACHE_LOG_DIR}/numera_error.log
    CustomLog ${APACHE_LOG_DIR}/numera_access.log combined
</VirtualHost>
```

### Enable the Site

```bash
sudo a2dissite 000-default.conf
sudo a2ensite numera.conf
sudo systemctl reload apache2
```

Apache now routes all traffic through Django's `wsgi.py`.

---

## ✅ Final Result

- ✅ Django application successfully served via Apache
- ✅ Templates rendered correctly
- ✅ Static files mapped properly
- ✅ Apache now translates HTTP → Python via WSGI

---

## 📚 Key Lessons Learned

1. **Apache ≠ Python** - Apache alone cannot execute Python code
2. **Django templates cannot be served directly** - They need Python execution
3. **WSGI is mandatory for Django + Apache** - It's the critical bridge
4. **Cloud provisioning is much faster than local installs** - Optimized mirrors make a difference
5. **Understanding architecture matters more than copying commands** - Know what you're doing, not just how
