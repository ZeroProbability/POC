def addToCount(String s) {
    def sortedList = s.toCharArray().toList().sort()
    sortedList += ['.']
    def prevChar = ''
    def repeatCount = 1
    def twoCountExists = false
    def threeCountExists = false
    for(def c: sortedList) {
       /// println "${c} ${prevChar} ${repeatCount}"
       if(c == prevChar) {
          repeatCount++ 
       } else {
          if(repeatCount == 2) {
             twoCountExists = true
          }
          if(repeatCount == 3) {
             threeCountExists = true
          }
          repeatCount = 1
          if(twoCountExists && threeCountExists) {
             break
          }
       }

       prevChar = c
    }
    return [twoCountExists, threeCountExists]
}

def file = '/home/anbu/poc/CodeChallenge/AOC2018/prob2_input.txt'

def twoCount = 0
def threeCount = 0
for(def str: new File(file).readLines()) {
    def (twoExists, threeExists) = addToCount(str)
    if(twoExists) twoCount++ 
    if(threeExists) threeCount++
}
println("${twoCount * threeCount}")
