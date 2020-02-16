class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dict1 = {'a' : ".-",'b' : "-...", 'c' : "-.-.", 'd':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        
        
        results = set()
        
        for i in range(len(words)):
            result = ""
            for j in range(len(words[i])):
                result += dict1[words[i][j]]
                
            results.add(result)
                
        return(len(results))