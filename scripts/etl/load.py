#!/usr/bin/env python
# coding: utf-8

# In[3]:

from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import urllib.parse
import os
from pathlib import Path

def get_engine():
    # Load environment variables
    env_path = Path(".").resolve() / ".env"
    load_dotenv(dotenv_path=env_path)

    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "3306")
    db = os.getenv("DB_NAME", "noodles_dw")

    # Encode password (important if it contains @, #, $, etc.)
    password = urllib.parse.quote_plus(password)

    try:
        engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}",
            echo=False,
            pool_pre_ping=True,
        )
        # Test the connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print(f"✅ Connected successfully to database: {db} at {host}:{port}")
        return engine

    except Exception as e:
        print("❌ Database connection failed.")
        print(f"Error details: {e}")
        raise


# In[2]:


get_ipython().system('pip install sqlalchemy pymysql python-dotenv')


# In[4]:


from etl.load import get_engine

engine = get_engine()


# In[8]:


from etl.load import get_engine


# In[9]:


import sys, os
# Adjust this path if your notebook is one level deeper or higher
sys.path.append(os.path.abspath('../scripts'))


# In[10]:


from etl.load import get_engine
engine = get_engine()


# In[11]:


sys.path.append(os.path.abspath('../../scripts'))


# In[13]:


import os
import urllib.parse
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

print("✅ Libraries imported successfully")


# In[14]:


def get_engine():
    """
    Creates and returns a SQLAlchemy engine to connect to a MySQL database.
    Uses environment variables from .env.
    """

    load_dotenv()
    # Load environment variables from .env file in the project root

    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "3306")
    db = os.getenv("DB_NAME", "noodles_dw")

    # Encode special characters in password
    password = urllib.parse.quote_plus(password)

    # Create SQLAlchemy engine
    engine = create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}",
        echo=False,
        pool_pre_ping=True
    )

    # Test connection
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print(f"✅ Connected successfully to database: {db} at {host}:{port}")
    except Exception as e:
        print("❌ Database connection failed.")
        print(f"Error details: {e}")
        raise

    return engine


# In[15]:


engine = get_engine()


# In[16]:


get_ipython().system('pip install sqlalchemy pymysql python-dotenv')


# In[17]:


import ipywidgets as widgets
from IPython.display import display, clear_output

# optional display widget
display(widgets.HTML("<b>Engine created and ready for reuse ✅</b>"))


# In[18]:


# Add scripts directory to Python path (for hybrid .ipynb/.py)
import sys, os
sys.path.append(os.path.abspath("../scripts"))
print(sys.path[-1])


# In[19]:


import sys, os
# Go two levels up, from current notebook (/scripts/etl)
sys.path.append(os.path.abspath('../../scripts'))
print(sys.path[-1])


# In[20]:


from etl.load import get_engine
engine = get_engine()


# In[21]:


# get_engine is already defined in memory
engine = get_engine()


# In[22]:


# Dynamically import code from a Jupyter notebook
import nbformat




# In[23]:




# In[24]:


from etl.load import get_engine


# In[25]:





# In[26]:


import os
print(os.getcwd())


# In[27]:


sys.path.append(os.path.abspath('../../scripts'))
from etl.load import get_engine
engine = get_engine()


# In[ ]:




