n = int(input())

while True:

   m = int(input())

   if m == 0:

      break

   else:

      if m%n != 0:

         print("%d is NOT a multiple of %d." %(m, n))

      else:

         print("%d is a multiple of %d." %(m, n))

      