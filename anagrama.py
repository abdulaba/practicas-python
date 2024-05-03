def anagrama(first_word, second_world):
  count = 1
  if len(first_word) == len(second_world):
    for letter in second_world:
      if first_word.find(letter):
        count += 1
        print(count)
  if count == len(first_word):
    print("Es anagrama")
  else:
    print("No es anagrama")

anagrama("amor", "roma")