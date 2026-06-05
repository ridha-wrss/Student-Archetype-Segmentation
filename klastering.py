# import pandas as pd
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.cluster import KMeans
# from sklearn.decomposition import PCA
# import joblib

# df = pd.read_excel('Data/Konsultasi Karir_28May26.xlsx')

# df = df[["Skor M2 (Skills)",
#          "Skor M5 (Compass)",
#          "Skor M8 (Ambisi)",
#          "Skor M9 (Resiliensi)",
#          "Semester",
#          "IPK",
#          "Ekspektasi Gaji",
#          "Minat Wirausaha",
#          "Rencana S2/Sertifikasi",
#          "Frekuensi Belajar",
#          "Level Bahasa Inggris",
#          "Motivasi",
#          "Cognitive Style",
#          "Work Style",
#          "Kultur Kerja",
#          "Ukuran Perusahaan"]]

# kolom_numerik_cluster = [
#     'Skor M2 (Skills)', 'Skor M5 (Compass)', 'Skor M8 (Ambisi)', 'Skor M9 (Resiliensi)',
#     'Semester', 'IPK', 'Ekspektasi Gaji', 'Minat Wirausaha',
#     'Rencana S2/Sertifikasi', 'Frekuensi Belajar', 'Level Bahasa Inggris'
# ]

# kolom_kategori_cluster = [
#     'Motivasi', 'Cognitive Style', 'Work Style', 'Kultur Kerja', 'Ukuran Perusahaan'
# ]

# ct = ColumnTransformer(
#     transformers=[
#         ('ohe', OneHotEncoder(handle_unknown= 'ignore'), kolom_kategori_cluster),
#         ('scale', StandardScaler(), kolom_numerik_cluster)
#     ])

# df_transform = ct.fit_transform(df)

# pca = PCA(n_components= 2)
# X_pca = pca.fit_transform(df_transform)

# df['PCA1'] = X_pca[:, 0]
# df['PCA2'] = X_pca[:, 1]

# k_optimal = 3
# kmeans = KMeans(n_clusters=k_optimal, random_state=42, n_init= 10)

# df['Cluster'] = kmeans.fit_predict(df_transform)

# cluster_summary_num = df.groupby('Cluster')[kolom_numerik_cluster].mean().round(2)
# cluster_summary_cat = df.groupby('Cluster')[kolom_kategori_cluster].agg(lambda x: x.value_counts().index[0])
# cluster_summary = pd.concat([cluster_summary_num, cluster_summary_cat], axis=1)

# cluster_summary['Persentase Mahasiswa'] = (df['Cluster'].value_counts(normalize=True) * 100).round(2).astype(str) + '%'

# # Menyimpan
# df.to_csv('Data/Hasil_Clustering.csv', index=False)
# cluster_summary.to_csv('Data/Summary_Clustering.csv', index=False)

# joblib.dump(ct, "Model/transformer.pkl")
# joblib.dump(kmeans, 'Model/kmeans.pkl')
# joblib.dump(pca, 'Model/pca.pkl')