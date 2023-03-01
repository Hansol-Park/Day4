## Day 4
## Time to Code.

#021 문자열 인덱싱
#letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.

lang = 'python'
print(lang[0],lang[2])

#022 문자열 슬라이싱
#자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.

license_plate = "24가 2210"
print(license_plate[-4:])

#023 문자열 인덱싱
#아래의 문자열에서 '홀' 만 출력하세요.

string = "홀짝홀짝홀짝"
print(string[::2])

#024 문자열 슬라이싱
#문자열을 거꾸로 뒤집어 출력하세요.

string2 = "PYTHON"
print(string2[::-1])

#025 문자열 치환
#아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.

Phone_Number = "010-2657-1494"
Phone_Number1 = Phone_Number.replace("-"," ")
print(Phone_Number1)

#026 문자열 다루기
#25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.

Phone_Number2 = Phone_Number.replace("-","")
print(Phone_Number2)

#027 문자열 다루기
#url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.

url = "http://sharebook.kr"
url_split = url.split(".")
print(url_split[-1])

#028 문자열은 immutable
#아래 코드의 실행 결과를 예상해보세요.

lang = "python"
#lang[0] = "P" #오류 발생 - 문자열은 변경 불가.
print(lang)

#029 replace 메서드
#아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.

string = "abcd"
string.replace("b","B")
print(string)

#`abcd`가 그대로 출력됩니다. 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문입니다. replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.

string_replacement = string.replace("b","B")
print(string_replacement)

#029 replace 메서드
#아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.

string = 'abcdfe2a354a32a'
string_replacement = string.replace('a',"A")
print(string_replacement)

#030 replace 메서드
#아래 코드의 실행 결과를 예상해보세요.

string = "abcd"
string.replace('b',"B")
print(string)
