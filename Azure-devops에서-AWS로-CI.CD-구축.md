[[_TOC_]]
# 딱히


# AWS Toolkit for Azure DevOps 설치

![image.png](/.attachments/image-fe9bfdf0-3321-496b-aa50-fd3ff704626b.png)
azure devops에서 오른쪽에 보면 쇼핑백 같은게 있다. 누르면 Browse marketplace가 있다. 그걸 클릭

![image.png](/.attachments/image-a0a95750-8fc9-4af6-bbcf-a1f162b23dca.png)
거기서 aws검색하면 aws toolkit이 있다 클릭

![image.png](/.attachments/image-c077de68-334d-4dcf-b4e5-050fe284612b.png)

![image.png](/.attachments/image-d188cf70-7db3-4de1-937e-8f0d8bc87381.png)

get it free를 누르면 azure devops에 직접설치하는 방법과 다운받는 방식이 있는데 난 이미 설치가되어 있다고 나와있다.(권한이 없으면 요청하라고 떠있다.)

# Aws service connection
![image.png](/.attachments/image-81d6b72b-264f-488c-ba63-d6e7cf35002b.png)
Project settings - Pipelines - Service connection 에서 오른쪽 위를 보면 New service connection 이 있다. 클릵

![image.png](/.attachments/image-390fe3ec-cec6-4b83-b7d4-438170df80d6.png)

![image.png](/.attachments/image-5a4f55eb-1fe6-4b86-b0ef-331d9f12dca1.png)
클릭하면 aws 를 누르고 만들어 놓았던 aws iam의 Access Key ID와 Secret Access Key를 입력하고 저장하면 인증 설정을 완료 했다. (pipeline 만들면서 만들어도 되긴하다)



# pipeline 구축
파이프 라인 탭에서 new pipeline 선탥
![image.png](/.attachments/image-44d17fdf-e965-4649-a815-ed1273ccd01f.png)

여기서 아래에 Use the classic editor를 클릭한다.

![image.png](/.attachments/image-5dd6af74-2521-4ab7-8296-7e025a501e5e.png)

source 를 선택하는데 azure repos git에 있으므로 선택하고 나머지 사항을 선택한후 Continue

![image.png](/.attachments/image-5446a133-50f7-4101-957f-6514500144b0.png)

그다음 ASP.NET을 선택한뒤 Apply 클릭

![image.png](/.attachments/image-71ecf8ad-a408-4dd2-8bf2-b2312f970008.png)

그다음 agent job1 옆에 +를 클릭하면 항목이 여러개 나오는데 
거기서 AWS Lambda Deploy Function을 클릭후 Add를 누른다.

![image.png](/.attachments/image-47565205-e77a-4df4-9c37-e276b48cf47c.png)

AWSCredentials는 전에 만들었던 걸 넣고 Region은 쓸 lambda가 저장되어 있는 region 선택, 수정만이 아닌 생성, 환경설정하고 싶으면 오른쪽 라디오 버튼을 누르면된다. 
function name은 있는거 있는거 수정할거면 그 이름을 적으면된다.
마지막으로 zip파일을 올려주면된다.

그리고 save& run을 하면 pipeline 구축 완료

# CI/CD 구축

![image.png](/.attachments/image-138fc8cb-650f-4cdd-9adf-6649cb2665a9.png)

triggers 에서 enable continous integreation을 선택하면 CI/CD 구축 완료!


> Function name 에러 날때 있는데 그때 권한 설정이 안되어 있으므로 들어가는 권한을 확인해주자.


 
