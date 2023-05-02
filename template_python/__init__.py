"""apens um teste de pacote"""

from dynaconf import settings as env


# Carrega .env que define o ambiente Ex: development, production

# log.debug(ENV['tt'])
print(env.NUMBER)
print(env.SENHA)
