def solution(text, ending):
  # return text[-len(ending):] == ending
  return text.endswith(ending)