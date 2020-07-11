import csa_env

def main():
  var = csa_env.get()
  print(var)
  csa_env.set({
    "a": "xxx"
  })
  var = csa_env.get()
  print(var)