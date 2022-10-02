def reverse(sequence): 
    sequence_type = type(sequence) 
    empty_sequence = sequence_type() 
      
    if sequence == empty_sequence: 
        return empty_sequence 
      
    rest = reverse(sequence[1:]) 
    first_sequence = sequence[0:1] 
      
    # Combine the result 
    final_result = rest + first_sequence
      
    return final_result 
  
# Driver code 
print(reverse([10, 20, 30, 40])) 
print(reverse("GeeksForGeeks")) 

