import sys
def main():
  if len(sys.argv) < 3:
    print("Uso: python bienvenidos.py <param1> <param2>")
    sys.exit(1)

  nombre=sys.argv[1]
  apellido=sys.argv[2]
  print ('Su nombre es: ' + nombre + ' ' + apellido)

if __name__ == "__main__":
   main()
