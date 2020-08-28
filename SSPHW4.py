import numpy as np

la=0.154

def edge(h, k, l, t):
   return (la/(2*np.sin((t*2*np.pi)/360))) * np.sqrt(h**2 + k**2 + l**2)

    

angle_list_1=[8, 23/2, 14, 33/2, 18, 20]
angle_list_2=[39/2, 45/2, 33, 79/2, 42]


# for t in angle_list_1:
#    for h in range(0,4,1):
#        for k in range(0,4,1):
#           for l in range(0,4,1):
#             edgestore = edge(h, k, l, t)
#             print("miller indices: ({},{},{}), angle: {}, edge length: {}".format(h, k, l, t, edgestore))

for t in angle_list_2:
   for h in range(0,4,1):
      for k in range(0,4,1):
         for l in range(0,4,1):
            edgestore = edge(h, k, l, t)
            print("miller indices: ({},{},{}), angle: {}, edge length: {}".format(h, k, l, t, edgestore))
# for t in angle_list_2:
#     list = []
#     for h in range(0,4,1):
#         for k in range(0,4,1):
#             for l in range(0,4,1):
#                 list.append(edge(h,k,l,t))
#     print(set(list))