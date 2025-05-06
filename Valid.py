import re

import re._compiler

class Valid:
  """
  Validate a ZIP code. return true if the input is a valid ZIP, 
  false otherwise.

  input: string
  output: boolean

  TODO: implement a method to validate a ZIP code
  """
  @staticmethod
  def zip(input):
    #length?
    if len(input) != 5:
      print("Zip length is invalid!")
      return False
    #digits?
    if not input.isdigit():
      print("Enter numbers for Zip")
      return False
    #real ZIP?
    
    return True
  
  """
  Validate a ZIP code. return true if the input is a valid ZIP, 
  false otherwise.

  input: string
  output: boolean

  TODO: implement a method to validate a ZIP code
  """
  @staticmethod
  def phone(input):
    #length?
    if len(input) != 10:
      print("invalid Phone# length")
      return False
    #digits?
    if not input.isdigit():
      print("Enter numbers for Phone#")
      return False
    #format?
    reg = r'^\+[0-9]{1,3} \([0-9]{3}\) [0-9]{3}-[0-9]{4}$'

    if not re.match(reg,input):
      print("Invalid phone number try something like 555-666-7777")
      return False
   
    
    return True