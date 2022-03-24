def check(i,j,k):

   O = ["C", "B", "A", "B", "B", "D", "A", "D", "B", "B"]
   print(i)

   print(j)

   answer=input().upper()
   if(O[k]==answer):

      print("CORRECT ANSWER\n")
   else:
      print("WRONG ANSWER")

      print("The correct answer is ",O[k],"\n")



Q=["1.How many red blood cells does the bone marrow produce every second?",
   "2.'RH' factor is a term that we hear in connection with",
   "3.The branch of Science which shows inter-relationship of living organism and their environment is",
   "4.Which of the following causes Poliomyelitis?",
   "5.Deforestation in the uplands may cause pollution in rivers through",
   "6. Toxin is a poisonous substance produce by",
   "7. Night blindness is caused by the deficiency of",
   "8. Exposure to sunlight helps a person improve his health because",
   "9. Chocolates can be bad for health because of high content of",
   "10. Small amounts of iodine are necessary in our diet to"]


A=["(A)5 million (B)7 million (C)10 million (D)12 million",
   "(A) Space Travel (B) Blood Transfusion (C) Air Pressure (D) Blood Pressure",
   "(A) Ecology (B) Genetics (C) Anatomy (D) Cell Biology",
   "(A) Dengue virus(B) Enterovirus(C) Mumps virus(D) Rhabdovirus",
   "(A) Leaching of salts(B) Erosion and silting(C) Inflow of forest material(D) Increased discharge rate",
   "(A) Some higher plants(B) Certain animals(C) Pathogenic bacteria(D) All of the above",
   "(A) Vitamin A(B) Vitamin B(C) Vitamin C(D) Vitamin D",
   "A) The infrared light kills bacteria in the body(B) Resistance power increases(C) The pigment cells in the skin get stimulated and produce a healthy tan(D) The ultraviolet rays convert skin oil into Vitamin D",
   "(A) Cobalt(B) Nickel(C) Zinc(D) Lead",
   "(A) Prevent pellagra(B) Compensate for under-active the thyroid gland(C) Stimulate clotting of blood(D) Stimulate pituitary gland"]
for k in range(0,10):
   i=Q[k]
   j=A[k]
   check(i,j,k)
