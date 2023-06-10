def main(*r):
  s = ({'GLSL', 'TWIG', 1970},
      {'GLSL', 'TWIG', 1979},
      {'GLSL', 'COQ'},
      {'GLSL', 'SAS', 1970},
      {'GLSL', 'SAS', 1979},
      {'RUST'},
      {'IDL', 1958, 'TWIG'},
      {'IDL', 1958, 'COQ'},
      {'IDL', 1958, 'SAS'},
      {'IDL', 1964, 'TWIG'},
      {'IDL', 1964, 'COQ'},
      {'IDL', 1964, 'SAS'})
  s1 = set(*r)
  return [i for i in range(len(s)) if not(len(s[i] - s1))][0] 
