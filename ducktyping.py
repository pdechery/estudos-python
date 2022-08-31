# Duck Typing

# Python não se preocupa com o tipo do objeto, somente verifica o método sendo executado nele.
# Também chamado Dynamic Typing

class Pessoa:
  def __len__(self):
    return "Eu"

nome = "Pierre"
idade = 46
stack = {
  "so":"Linux",
  "distro":"Ubuntu",
  "programming": ['Python','Javascript'],
  "framweworks": ['Django','Flask','Wagtail'],
}