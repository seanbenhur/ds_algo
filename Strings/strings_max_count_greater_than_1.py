"""Got this question in CaterPillar OA"""


from collections import Counter
def dictWords(textInput):
	# Write your code here
    textInput = list(textInput.split( ))
    counts = Counter(textInput)
    keys = list(counts.keys())
    values = list(counts.values())
    ans = []
    for key,value in zip(keys,values):
        if value > 1:
            ans.append(key)
            
    return ans
            
def main():
	#input for textInput
	textInput = "cat batman latt matter cat matter cat"
	result = dictWords(textInput)
	print(" ".join([str(res) for res in result]))	

if __name__ == "__main__":
	main()