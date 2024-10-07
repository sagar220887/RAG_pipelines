

def calculate_jaccard_index(set_a, set_b):
    # Calculate the intersection of two sets
    intersection = set_a.intersection(set_b)
    print('intersection - ', intersection)
    
    # Calculate the union of two sets
    union = set_a.union(set_b)
    print('union - ', union)
    
    # Calculate the Jaccard index
    print('len(intersection) - ', len(intersection))
    print('len(union) - ', len(union))
    jaccard_index = len(intersection) / len(union)
    print(f'Jaccard Index :: {len(intersection)}/{len(union)} = ', jaccard_index)
    
    return jaccard_index


def get_jaccard_similarity_for_strings(str1, str2, n_gram=2):
    str1_lower = str1.lower().replace(' ', '')
    str1_ngrams = set([str1_lower[i:i + n_gram] for i in range(len(str1_lower) - n_gram + 1)])

    str2_lower = str2.lower().replace(' ', '')
    str2_ngrams = set([str2_lower[i:i + n_gram] for i in range(len(str2_lower) - n_gram + 1)])
    
    jaccard_index = calculate_jaccard_index(str1_ngrams, str2_ngrams)
    return jaccard_index



if __name__ == '__main__':
    ## Example - 1
    # A = {1,3, 5, 7, 9}
    # B = {1,3, 5, 7, 8}
    
    # jaccard_index = calculate_jaccard_index(A, B)
    # print(f"The Jaccard index of sets A and B is: {jaccard_index}")


    ## Example - 2
    # A = "Phnom Penh"
    # B = "Phnum Penh"
    # C = "Paris"

    # # Converting the strings ito 2-gram
    # a_lower = A.lower().replace(' ', '')
    # print('a_lower - ', a_lower)
    # set_A = {'ph', 'no', 'mp', 'en','h'}

    # b_lower = B.lower().replace(' ', '')
    # print('b_lower - ', b_lower)
    # set_B = {'ph', 'nu', 'mp', 'en','h'}

    # c_lower = C.lower().replace(' ', '')
    # print('c_lower - ', c_lower)
    # set_AC = {'pa', 'ri', 's'}

    # J_a_b = calculate_jaccard_index(set_A, set_B)



    ## Example 3:
    A = "I like blue tie"
    B = "I like blue shirt"
    get_jaccard_similarity_for_strings(A, B)



    ## Example - 4: FAILS
    A = "the man is chasing the dog"
    B = "the dog is chasing the man"
    get_jaccard_similarity_for_strings(A, B)