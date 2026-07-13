# Write a Python program to find the first non-repeating character in a string.

# def find_first_unique_char(text):
#     text = text.lower();
#     freq = {};
#     for i in text:
#         if i in freq:
#             freq[i] += 1;
#         else:
#             freq[i] = 1;
            
    
#     for i in freq:
#         if freq[i] == 1:
#             return i;
        
#     return None;
    
# print(find_first_unique_char('Samples'))

# ================================================================================================

# Write a Python program to capitalize the first and last character of each word in a string.

# def make_capitalize_words(sentence):
#     sentence = sentence.split(' ');
#     result  = '';
    
#     for word in sentence:
#         result += word[0].upper() +  word[1:-1] + word[-1].upper() + ' ';
    
#     return result;
# print(make_capitalize_words('wow fantastic item'));

# ================================================================================================

# Fibonacci Sequence up to N terms

# def fibonacci(count):
#     fibSeries = [0,1];
#     for i in range(0, count-2):
#         length = len(fibSeries);
#         fibSeries.append(fibSeries[length - 1] + fibSeries[length - 2]);
    
#     return fibSeries;
# print(fibonacci(5));

# ================================================================================================
