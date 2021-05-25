from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

nome = 'ACHILLES LIGABO JUNIOR'
cref = '019583-G/SP'


def getCref():
    input_element = driver.find_element_by_xpath('/html/body/section/div/div/div[2]/div/div/div[1]/label/input')
    input_element.send_keys(cref)
    sleep(1)
    search = driver.find_elements_by_xpath('/html/body/section/div/div/div[2]/div/div/table/tbody/tr')
    for tr in search:
        tds = tr.find_elements(By.TAG_NAME, 'td')
        result = {'Cref': tds[1].text.split(" ")[1],
                  'Nome': tds[2].text}

    if result['Nome'] == nome and result['Cref'] == cref:
        print('CREF Válido')
    else:
        print('CREF Inválido')

    print('Nome e Cref validado -> {}, {}'.format(nome, cref))
    print(result)


try:
    #Executa o script abrindo o navegador
    #driver = webdriver.Chrome()

    #Executa o script sem abrir o navegador
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options = op)

    url = 'https://www.confef.org.br/confef/registrados/'
    driver.get(url)
    getCref()

finally:
    driver.close()
