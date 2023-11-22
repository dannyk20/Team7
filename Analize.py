import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV 파일 불러오기
csv_file_path = 'cox-violent-parsed_filt_usable.csv'
df = pd.read_csv(csv_file_path)

# 성별과 재범 발생 여부 사이의 상관 관계를 나타내는 데이터프레임 생성
gender_recid_corr = pd.crosstab(df['sex'], df['is_recid'])

# 인종과 재범 발생 여부 사이의 상관 관계를 나타내는 데이터프레임 생성
race_recid_corr = pd.crosstab(df['race'], df['is_recid'])

# 그래프 그리기 (서브플롯 사용)
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# 성별과 재범 발생 여부 관계 그래프
sns.barplot(x=gender_recid_corr.index, y=gender_recid_corr[1], ax=axes[0])
axes[0].set_title('Correlation between Gender and Recidivism')
axes[0].set_xlabel('Gender')
axes[0].set_ylabel('Number of Recidivism Cases')

# 인종과 재범 발생 여부 관계 히트맵
sns.heatmap(race_recid_corr, annot=True, fmt='d', cmap='Blues', cbar_kws={'label': 'Number of Recidivism Cases'}, ax=axes[1])
axes[1].set_title('Correlation between Race and Recidivism')
axes[1].set_xlabel('Recidivism')
axes[1].set_ylabel('Race')

# 이미지 파일로 저장
plt.tight_layout()
plt.savefig('static/correlation_graphs.png')
plt.show()
