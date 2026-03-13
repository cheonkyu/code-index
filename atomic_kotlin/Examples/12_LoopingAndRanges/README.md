# 12. LoopingAndRanges: 반복문과 범위 이해하기

안녕하세요! 이번 챕터에서는 코틀린에서 반복문을 사용하는 방법과 범위(range)에 대해 배워볼게요. 초보자분들을 위해 친절하게 설명해드릴게요.

## 반복문 이해하기: `for` 키워드 사용하기

코틀린에서 `for` 키워드는 주어진 값의 시퀀스(sequence)를 순회하면서 코드 블록을 실행해줘요. 여기서 주로 사용하는 `in` 키워드는 특정 범위나 시퀀스의 각 요소를 차례대로 넘기며 루프를 진행하는 역할을 해요.

### 기본 반복문 예제

아래 예제는 `for` 루프를 이용해 특정 횟수만큼 동작을 반복하는 방법을 보여줘요:

```kotlin
fun main() {
    for (i in 1..3) {  // 1부터 3까지의 범위
        println("Hey $i!")
    }
}
/* 출력:
Hey 1!
Hey 2!
Hey 3!
*/
```

**설명**:
- `for (i in 1..3)`에서 `i`는 1부터 시작해서 3까지 차례대로 증가해요.
- 각 루프 실행 시 `i`는 다음 값을 받아 "Hey i!"를 출력해요.

### 범위 정의하기

코틀린에서는 정수 범위를 다양한 방법으로 정의할 수 있어요:

#### 기본 범위 정의
```kotlin
fun main() {
    val range1 = 1..10   // 1부터 10까지 포함 (양쪽 경계 포함)
    val range2 = 0 until 10  // 0부터 9까지 포함 (마지막 값 미포함)
    println(range1)   // 출력: 1..10
    println(range2)   // 출력: 0..9
}
/* 출력:
1..10
0..9
*/
```

- `..`은 양쪽 경계값을 포함하는 범위를 만듭니다.
- `until`은 끝 값을 제외하고 범위를 만듭니다.

### 범위를 이용한 합계 계산

범위를 이용해 특정 범위 내의 숫자 합계를 계산할 수도 있어요:

```kotlin
fun main() {
    var sum = 0
    for (n in 10..100) {  // 10부터 100까지의 숫자 합계
        sum += n
    }
    println("합계 = $sum")  // 출력: 합계 = 5005
}
```

**설명**:
- `for (n in 10..100)`에서 `n`은 10부터 100까지 순회하며 `sum`에 누적해요.

### 반복 순서와 간격 조정하기

#### 순서 변경 및 간격 설정
```kotlin
fun showRange(r: IntProgression) {
    for (i in r) {
        print("$i ")
    }
    println("\n$r")
}

fun main() {
    showRange(1..5)          // 1부터 5까지 기본 간격
    showRange(0 until 5)     // 0부터 4까지 (마지막 값 미포함)
    showRange(5 downTo 1)   // 5부터 1까지 감소
    showRange(0..9 step 2)  // 0부터 9까지 간격 2
    showRange(0 until 10 step 3)  // 0부터 9까지 간격 3
    showRange(9 downTo 2 step 3) // 9부터 2까지 간격 3 감소
}
/* 출력:
1 2 3 4 5
1..5
0 1 2 3 4
0..9 step 2
0 2 4 6 8
9 downTo 2 step 3
9 6 3
*/
```

**설명**:
- `downTo`는 감소하는 범위를 만들어요.
- `step`을 사용하면 간격을 조절할 수 있어요.

### 문자 범위와 문자열 인덱스 활용

#### 문자 범위 반복
```kotlin
fun main() {
    for (c in 'a'..'z') {  // 'a'부터 'z'까지 문자 반복
        print(c)
    }
}
/* 출력:
abcdefghijklmnopqrstuvwxyz
*/
```

#### 문자열 인덱스 접근
```kotlin
fun main() {
    val s = "abc"
    for (i in 0..s.lastIndex) {  // 문자열 s의 인덱스 순회
        print(s[i] + 1)  // 문자 코드 +1
    }
}
/* 출력:
bcd
*/
```

**설명**:
- 문자열의 인덱스는 `0`부터 시작하므로 `s[i]`로 각 문자에 접근할 수 있어요.
- 문자 코드에 정수를 더하면 새로운 문자를 얻을 수 있어요.

#### 문자 비교하기
```kotlin
fun main() {
    val ch: Char = 'a'
    println(ch + 25)  // 문자 코드에 정수 더하기
    println(ch < 'z')  // 문자 비교하기
}
/* 출력:
z
true
*/
```

### 문자열 직접 반복하기
```kotlin
fun main() {
    for (ch in "Jnskhm ") {  // 문자열 직접 반복
        print(ch + 1)  // 각 문자에 정수 더하기
    }
}
/* 출력:
Kotlin!
*/
```

### 문자열 내 특정 문자 찾기

만약 문자열 내에서 특정 문자가 있는지 확인하고 싶다면 다음과 같이 할 수 있어요:

```kotlin
fun hasChar(s: String, ch: Char): Boolean {
    for (c in s) {
        if (c == ch) {
            return true  // 문자를 찾으면 즉시 반환
        }
    }
    return false  // 찾지 못하면 false 반환
}

fun main() {
    val result = hasChar("hello", 'l')  // "hello"에서 'l' 찾기
    println("문자열에 있는지: $result")  // 출력: 문자열에 있는지: true
}
```

### 핵심 개념 요약

1. **반복문**: `for (변수 in 범위)`로 쉽게 반복 가능해요.
2. **범위 정의**: `..`은 양쪽 경계 포함, `until`은 마지막 값 미포함이에요.
3. **간격 조절**: `step`을 사용하면 원하는 간격으로 순회 가능해요.
4. **문자 처리**: 문자는 숫자로 취급되어 코드값을 이용해 조작 가능해요.
5. **문자열 인덱스**: 문자열의 각 문자는 인덱스를 통해 접근 가능해요.

이 내용들이 코틀린에서 반복문과 범위를 이해하는 데 도움이 되길 바라요! 더 궁금한 점이 있으면 언제든지 물어봐요!