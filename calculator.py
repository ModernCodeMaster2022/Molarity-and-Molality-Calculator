from os import system, name
import numbers
import re

#Global variables defined here
rows, cols = (10, 2)
gElementList = [[""] * cols] * rows
weightList = [""] * 10
soluteList = [""] * 10
solventList = [""] * 10
soluteWeight = 0
solventWeight = 0
solutionWeight = 0
soluteUnit = ""
solventUnit = ""
opChoice = ""
solutionUnit = ""

# Clears terminal
def clr_term():
  if name == "nt":
    system("cls")
  else:
    system("clear")


# Following function prints help menu
def printHelpMenu():
  print("Find the Right Formula for you!")
  print(
    "NOTE: It is expected that user will enter a correct Solute and Solvent")
  print("How to Use:")
  print("\n" +
        "1. You have two formulas to choose from, Molarity and Molality.")
  print(
    "\n" +
    "2. You can input m if you want to solve for molality and M if you want to solve for Molarity."
  )
  print(
    "\n" +
    "3. Solute is the powder being dissolved and solvent is the item doing the dissolving."
  )
  print("\n" + "4. Molality = moles of solute/kg of solvent ")
  print("\n" + "5. Molarity = moles of solute/liters of solution ")
  print(
    "\n" +
    "6. You have two formulas to choose from, Molarity and Molality. In order to  continue, input m for molality and M for molarity."
  )
  print("==================================================================")


#Periodic Table of Elements (Arranged from left to right starting top row)
symbols = [
  'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si',
  'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co',
  'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
  'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I',
  'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy',
  'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au',
  'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U',
  'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db',
  'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'
]
#Atomic weight given for each element
atomic_masses = {
  'H': 1.008,
  'He': 4.003,
  'Li': 6.941,
  'Be': 9.012,
  'B': 10.811,
  'C': 12.011,
  'N': 14.007,
  'O': 15.999,
  'F': 18.998,
  'Ne': 20.180,
  'Na': 22.990,
  'Mg': 24.305,
  'Al': 26.982,
  'Si': 28.086,
  'P': 30.974,
  'S': 32.066,
  'Cl': 35.453,
  'Ar': 39.948,
  'K': 39.098,
  'Ca': 40.078,
  'Sc': 44.956,
  'Ti': 47.867,
  'V': 50.942,
  'Cr': 51.996,
  'Mn': 54.938,
  'Fe': 55.845,
  'Co': 58.933,
  'Ni': 58.693,
  'Cu': 63.546,
  'Zn': 65.38,
  'Ga': 69.723,
  'Ge': 72.631,
  'As': 74.922,
  'Se': 78.971,
  'Br': 79.904,
  'Kr': 84.798,
  'Rb': 84.468,
  'Sr': 87.62,
  'Y': 88.906,
  'Zr': 91.224,
  'Nb': 92.906,
  'Mo': 95.95,
  'Tc': 98.907,
  'Ru': 101.07,
  'Rh': 102.906,
  'Pd': 106.42,
  'Ag': 107.868,
  'Cd': 112.414,
  'In': 114.818,
  'Sn': 118.711,
  'Sb': 121.760,
  'Te': 126.7,
  'I': 126.904,
  'Xe': 131.294,
  'Cs': 132.905,
  'Ba': 137.328,
  'La': 138.905,
  'Ce': 140.116,
  'Pr': 140.908,
  'Nd': 144.243,
  'Pm': 144.913,
  'Sm': 150.36,
  'Eu': 151.964,
  'Gd': 157.25,
  'Tb': 158.925,
  'Dy': 162.500,
  'Ho': 164.930,
  'Er': 167.259,
  'Tm': 168.934,
  'Yb': 173.055,
  'Lu': 174.967,
  'Hf': 178.49,
  'Ta': 180.948,
  'W': 183.84,
  'Re': 186.207,
  'Os': 190.23,
  'Ir': 192.217,
  'Pt': 195.085,
  'Au': 196.967,
  'Hg': 200.592,
  'Tl': 204.383,
  'Pb': 207.2,
  'Bi': 208.980,
  'Po': 208.982,
  'At': 209.987,
  'Rn': 222.081,
  'Fr': 223.020,
  'Ra': 226.025,
  'Ac': 227.028,
  'Th': 232.038,
  'Pa': 231.036,
  'U': 238.029,
  'Np': 237,
  'Pu': 244,
  'AM': 243,
  'Cm': 247,
  'Bk': 247,
  'Ct': 251,
  'Es': 252,
  'Fm': 257,
  'Md': 258,
  'No': 259,
  'Lr': 262,
  'Rf': 261,
  'Db': 262,
  'Sg': 266,
  'Bh': 264,
  'Hs': 269,
  'Mt': 268,
  'DS': 271,
  'Rg': 272,
  'Cn': 285,
  'Nh': 284,
  'Fl': 289,
  'Mc': 288,
  'Lv': 292,
  'Ts': 294,
  'Og': 294
}

#Validates if character is numeric
def isNumeric(x):
  try:
    float(x)
    return True
  except ValueError:
    return False

# Validates if letter is uppercase
def isCapital(ltr):
  if (ltr.isupper()):
    return True
  else:
    return False


#Calculates and returns molar mass for the given solute/solvent
def getMolarMass(myList):
  molarMass = 0
  localElem = ""
  localWeight = 0
  localFlag = ""
  #Iterates over the given list to extract the element
  # and its weight/multiplier
  for i in range(len(myList)):
    localElem = myList[i][0]
    if (localElem == ""):
      localFlag == 'done'
      break
    #If the element has no weight or multiplier, it is by
    # default set to 1
    if (localElem != ""):
      localWeight = int(myList[i][1])
      if (soluteUnit == "g" or soluteUnit == "Kg"):
        molarMass += atomic_masses.get(localElem) * localWeight
      else:
        molarMass = soluteWeight
  return molarMass


# Calculate solvent mass based on the given unit from the user
def getSolventMass(myList):
  solventMass = 0
  localElem = ""
  localMass = 0
  localFlag = ""
  #Iterates over the given list to extract elements and its multiplier
  for i in range(len(myList)):
    localElem = myList[i][0]
    if (localElem == ""):
      localFlag == 'done'
      break
    if (localElem != ""):
      localMass = int(myList[i][1])
      #solventMass is calculated based on the user
      #  input in this case "mol"
      if (solventUnit == "mol"):
        solventMass = getMolarMass(myList)
        solventMass = (solventMass * int(solventWeight)) / 1000
      #When solvent unit is in grams, it converts into kilo
      elif (solventUnit == "g"):
        solventMass = int(solventWeight) / 1000
      elif (solventUnit == "Kg"):
        solventMass = solventWeight
  return solventMass

# Performs unit conversion according to the given unit
def getSoluteMoles(weight, molarmass):
  if soluteUnit == "g":
    moles = weight / molarmass
  elif soluteUnit == "Kg":
    moles = (weight * 1000) / molarmass
  elif (soluteUnit == "mol"):
    moles = float(soluteWeight)
  return moles

# Performs unit verification for milliliters or liters
def solutionLiters(solution):
  if (solutionUnit == "mL"):
    solutionL = float(solution) / 100
    return solutionL
  elif (solutionUnit == "L"):
    solutionL = float(solution)
    return solutionL

# Takes solute and solvent and returns molality
def getMolality(solute, solvent):
  molality = float(solute) / float(solvent)
  return molality

# Takes solute and solution and returns molarity
def getMolarity(solute, solution):
  molarity = solute / solution
  return molarity


#Following function takes list as a parameter and parse it
#  to identy elements and weight
def identifyElem(user_inp):
  global gElementList  #to work with global variables in a function
  global weightList
  tmpElement = ""
  tmpWeight = ""
  nextElement = ""
  procFlag = ""
  loopIndex = 0

  # Takes the user input and converts into 2D list that contains element and
  # weight/multiplier
  for i in range(len(user_inp)):
    listLength = len(user_inp)
    lastElement = user_inp[-1]
    if (i == listLength - 1):
      procFlag = "finished"
      nextElement = ""
    if ((i + 1) <= listLength - 1):  #take the next element within boundary
      nextElement = user_inp[i + 1]
    #Stores individual element in a local variable.
    if (isNumeric(user_inp[i]) == False and isCapital(user_inp[i]) == True):
      tmpElement = user_inp[i]
    #Stores weight/multiplier for the particular element in the local variable
    if (isNumeric(user_inp[i])):
      tmpWeight += user_inp[i]
    #Identifies next element and flags the process is done for the previous element.
    if (isCapital(nextElement)):
      if (tmpElement != ""):
        if (tmpWeight == ""):
          tmpWeight = "1"
        procFlag = "done"
    elif (procFlag != "finished" and isNumeric(nextElement) == False):
      tmpElement += nextElement
    #When the flag is done, the element and the weight/multiplier is stored in the global 2D list.
    if (procFlag == "done"):
      gElementList.insert(loopIndex, [tmpElement, tmpWeight])
      loopIndex += 1
      tmpElement = ""
      tmpWeight = ""
      procFlag = ""
    #Process is finished when the last element is processed.
    if (procFlag == "finished"):
      if (tmpWeight == ""):
        tmpWeight = "1"
      gElementList.insert(loopIndex, [tmpElement, tmpWeight])
      loopIndex = 0

# The user input prompts are created and checked
def getUserInput():
  global gElementList  #to work with global variables in a function
  global weightList
  global soluteList
  global solventList
  global soluteWeight
  global solventWeight
  global solutionWeight
  global soluteUnit
  global solventUnit
  global opChoice
  global solutionUnit

  while (1):
    opChoice = input("Enter m for molality or M for molarity: ")
    if (opChoice == "m" or opChoice == "M"):
      break

  while (1):
    soluteInp = input("Enter the name of your solute: ")
    if (isCapital(soluteInp[0]) == True):
      soluteList = list(soluteInp)
      break
    else:
      input("Please enter a Valid Name for Solute:e.g H2O")
  while (1):
    soluteWeight = input("Enter Solute Weight: ")  # check if its numeric value
    if (isNumeric(soluteWeight) == False):
      input("Please enter a numeric Value..")
    else:
      break

  while (1):
    soluteUnit = input("Enter the Solute Unit(mol or g or Kg): ")
    if (soluteUnit != "mol" and soluteUnit != "g" and soluteUnit != "Kg"):
      print("Please enter mol, g or Kg...")
    else:
      break

  #While user solves for molality (m), the prompt will ask to enter solvent name, otherwise it will break for molarity
  while (1):
    if (opChoice == "m"):
      solvent = input("Enter the name of your solvent: ")
      if (isCapital(solvent[0]) == True):
        solventList = list(solvent)
        break
      else:
        print("Enter a valid solvent e.g. H2O")
        input("Press Enter to Continue")
    elif (opChoice == "M"):
      break

  #While user choice is molality (m), the prompt will ask to enter weight of solvent and if user choice is molarity(M), prompt will ask to enter weight of solution.
  while (1):
    if (opChoice == "m"):
      solventWeight = input(
        "Enter the Weight of the Solvent: ")  # Validate for number
      if (isNumeric(solventWeight) == False):
        input("Please enter a numeric Value..")
      else:
        break
    elif (opChoice == "M"):
      solutionWeight = input("Enter the weight of the Solution: ")
      if (isNumeric(solutionWeight) == False):
        input("Please enter a numeric Value..")
      else:
        break
  while (1):
    if (opChoice == "m"):
      solventUnit = input(
        "Enter the Solvent Unit (mol or g or Kg): ")  #Check for validity
      if (solventUnit != "mol" and solventUnit != "g" and solventUnit != "Kg"):
        print("Please enter mol, g or Kg...")
      else:
        break
    elif (opChoice == "M"):
      solutionUnit = input(
        "Enter the Solution Unit (L or mL): ")  #Check for validity
      if (solutionUnit != "L" and solutionUnit != "mL"):
        print("Please enter L or mL...")
      else:
        break

#Performs final calculations for molality
def calculateMolality():
  molarMass = getMolarMass(gElementList)
  soluteMole = getSoluteMoles(float(soluteWeight), float(molarMass))
  gElementList.clear()
  identifyElem(solventList)
  solventKg = getSolventMass(gElementList)
  molality = getMolality(soluteMole, solventKg)
  print(f'Your molality is: {molality:.5f} m')

#Performs final calculations for Molarity
def calculateMolarity():
  molarMass = getMolarMass(gElementList)
  soluteMole = getSoluteMoles(float(soluteWeight), float(molarMass))
  solutionLiter = solutionLiters(solutionWeight)
  molarity = getMolarity(soluteMole, solutionLiter)
  print(f'Your molarity is: {molarity:.5f} M')


#Whole program operates under this function
def main():
  printHelpMenu()
  getUserInput()
  identifyElem(soluteList)
  if (opChoice == 'm'):
    calculateMolality()
  elif (opChoice == 'M'):
    calculateMolarity()


main()
