# Python program to find
# maximal Bipartite matching.
 
class GFG:
    def __init__(self,graph):
         
        # grafik residu
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])
 
    # Fungsi rekursif berbasis DFS
    # yang mengembalikan true jika cocok
    # untuk simpul u dimungkinkan
    def bpm(self, u, matchR, seen):
 
        # Cobalah setiap pekerjaan satu per satu
        for v in range(self.jobs):
 
            # Jika pelamar Anda tertarik
            # dalam pekerjaan v dan v tidak terlihat
            if self.graph[u][v] and seen[v] == False:
                 
                # Tandai v sebagai telah dikunjungi
                seen[v] = True
 
                '''Jika pekerjaan 'v' tidak ditugaskan
                    pelamar ATAU ditugaskan sebelumnya
                    pelamar untuk pekerjaan v (yaitu matchR[v])
                    memiliki pekerjaan alternatif yang tersedia.
                    Sejak v ditandai sebagai dikunjungi di
                    baris di atas, matchR[v] berikut ini
                    panggilan rekursif tidak akan mendapatkan pekerjaan 'v' lagi'''
                if matchR[v] == -1 or self.bpm(matchR[v],
                                               matchR, seen):
                    matchR[v] = u
                    return True
        return False
 
    # Mengembalikan jumlah pencocokan maksimum
    def maxBPM(self):
        '''Array untuk melacak
            pelamar yang ditugaskan untuk pekerjaan.
            Nilai matchR[i] adalah
            nomor pelamar ditugaskan untuk pekerjaan i,
            nilai -1 menunjukkan tidak ada yang ditugaskan.'''
        matchR = [-1] * self.jobs
         
        # Jumlah pekerjaan yang diberikan kepada pelamar
        result = 0
        for i in range(self.ppl):
             
            # Tandai semua pekerjaan sebagai tidak terlihat untuk pelamar berikutnya.
            seen = [False] * self.jobs
             
            # Temukan apakah pelamar 'u' bisa mendapatkan pekerjaan
            if self.bpm(i, matchR, seen):
                result += 1
        return result
 
 
bpGraph =[[0, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1]]
 
g = GFG(bpGraph)
 
print ("Jumlah maksimum pelamar yang bisa mendapatkan pekerjaan adalah :  %d " % g.maxBPM())
 
# This code is contributed by Neelam Yadav