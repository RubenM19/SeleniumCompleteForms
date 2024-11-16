from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Ruta del driver
driver_path = 'C:\\Users\\ruben\\Desktop\\PROG\\chromedriver.exe'

# URL del formulario
url = 'https://forms.gle/6mPV1EYMjrnJZDAe8'

# Función para iniciar el navegador
def iniciar_navegador():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Función para llenar el formulario
def fill_forms(driver, ans_list):
    # Espera a que todos los grupos de preguntas se carguen
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "Qr7Oae"))
    )
    
    questionGroup = driver.find_elements(By.CLASS_NAME, "Qr7Oae")
    if questionGroup:
        questions = [q.find_elements(By.CLASS_NAME, "AB7Lab.Id5V1") for q in questionGroup]

    for i, answer in enumerate(ans_list):
        if i < len(questions) and questions[i] and len(questions[i]) > answer:
            questions[i][answer].click()

    # Encontrar y hacer clic en el botón de enviar
    submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span/span'))
    )
    submit.click()

# Llenado del formulario X veces
for i in range(5):
    # Iniciar el navegador en cada iteración
    driver = iniciar_navegador()
    driver.get(url)
    time.sleep(1)

    # Generar respuestas aleatorias para cada pregunta
    respuestas_aleatorias = [random.randint(0, 4) for _ in range(29)]
    fill_forms(driver, respuestas_aleatorias)

    # Cerrar el navegador después de cada llenado
    driver.quit()
    time.sleep(2)  # Tiempo de espera antes de la siguiente iteración
