# 27. Maps: 키와 값을 연결하는 맵 이해하기

안녕하세요! 오늘은 코틀린에서 맵(Maps)에 대해 배워볼게요. 맵은 마치 작은 데이터베이스처럼 작동하지만, 훨씬 간편하고 효율적이에요. 초보자도 쉽게 이해할 수 있도록 친절하게 설명해드릴게요.

## 기본 개념: 맵이란 무엇인가요?

맵은 **키(key)**와 **값(value)**을 연결해주는 데이터 구조예요. 특정 **키**를 주면 그에 해당하는 **값**을 찾아주는 역할을 합니다. 쉽게 말해, **사전**처럼 생각하면 돼요!

### 맵 생성하기

맵을 생성할 때는 `mapOf()` 함수를 사용해요. 키와 값을 쌍으로 제공하면 됩니다. 예를 들어:

```kotlin
fun main() {
    // 키와 값 쌍을 제공하여 맵 생성
    val 상수들 = mapOf(
        "Pi" to 3.141,
        "e" to 2.718,
        "phi" to 1.618
    )

    // 출력 예시: "{Pi=3.141, e=2.718, phi=1.618}"
    println(상수들) 

    // 특정 키의 값을 찾기
    println(상수들["e"] ?: "키가 없어요")  // 출력: 2.718

    // 맵의 키들만 가져오기
    println(상수들.keys)  // 출력: setOf("Pi", "e", "phi")

    // 맵의 값들만 가져오기
    println(상수들.values)  // 출력: [3.141, 2.718, 1.618]

    // 반복문을 사용해 키와 값 쌍을 순회
    var 문자열 = ""
    for ((키, 값) in 상수들) {
        문자열 += "$키=${값}, "
    }
    println(문자열)  // 출력: "Pi=3.141, e=2.718, phi=1.618,"
}
```

### 맵 순회하기

1. **키와 값 쌍 순회**:
   ```kotlin
   for ((키, 값) in 상수들) {
       // 각 키와 값을 직접 접근
       println("$키: $값")
   }
   ```

2. **키만 순회**:
   ```kotlin
   for (키 in 상수들.keys) {
       println("키: $키")
   }
   ```

## 맵의 종류: 읽기 전용 vs 변경 가능

### 읽기 전용 맵 (`mapOf`)

읽기 전용 맵은 내용을 변경할 수 없어요. 예를 들어:

```kotlin
fun main() {
    val 상수맵 = mapOf(5 to "five", 6 to "six")
    println(상수맵[5] ?: "키가 없어요")  // 출력: "five"
    // 상수맵[5] = "fiveive"  // 오류: 불가능
    // 상수맵 += (4 to "four")  // 오류: 불가능
    println(상수맵)  // 출력: mapOf(5 to "five", 6 to "six")
}
```

### 변경 가능 맵 (`mutableMapOf`)

변경 가능 맵은 내용을 추가하거나 수정할 수 있어요:

```kotlin
fun main() {
    val 가변맵 = mutableMapOf(5 to "five", 6 to "six")
    println(가변맵[5] ?: "키가 없어요")  // 출력: "five"
    가변맵[5] = "fiveive"  // 값 변경
    println(가변맵)  // 출력: mapOf(5 to "fiveive", 6 to "six")
    
    // 새로운 키-값 쌍 추가
    가변맵 += 4 to "four"
    println(가변맵)  // 출력: mapOf(5 to "fiveive", 6 to "six", 4 to "four")
}
```

## 맵에서 값 가져오기

읽기 전용 맵에서는 특정 키가 존재하지 않을 때 `getValue()`를 사용해 안전하게 값을 가져올 수 있어요:

```kotlin
fun main() {
    val 맵 = mapOf('a' to "attempt")
    println(맵['b'] ?: "키가 없어요")  // 출력: null

    try {
        capture {
            맵.getValue('b')
        }
    } catch (e: NoSuchElementException) {
        println(e.message)  // 출력: "Key b is missing in the map."
    }

    // 키가 존재하면 값을 가져오거나 디폴트 값을 반환
    println(맵.getOrDefault('a', "??"))  // 출력: "attempt"
    println(맵.getOrDefault('b', "??"))  // 출력: "??"
}
```

## 클래스 인스턴스 저장하기

맵에는 클래스 인스턴스도 저장할 수 있어요. 예를 들어, 연락처 정보를 맵에 저장해볼게요:

```kotlin
package maps

import atomictest.eq

class Contact(
    val 이름: String,
    val 전화번호: String
) {
    override fun toString(): String {
        return "Contact('$이름', '$전화번호')"
    }
}

fun main() {
    val miffy = Contact("Miffy", "1-234-567890")
    val cleo = Contact("Cleo", "098-765-4321")
    
    // 전화번호를 키로 연락처를 값으로 저장
    val 연락처맵 = mapOf(
        miffy.전화번호 to miffy,
        cleo.전화번호 to cleo
    )

    println(연락처맵["1-234-567890"] ?: "키가 없어요")  // 출력: Contact('Miffy', '1-234-567890')
    println(연락처맵["1-111-111111"] ?: "키가 없어요")  // 출력: 키 없음 (null)
}
```

## 요약

- **맵**은 키와 값을 연결해주는 데이터 구조입니다.
- **맵 생성**: `mapOf()` (읽기 전용), `mutableMapOf()` (변경 가능)
- **키와 값 접근**: `[]` 연산자 사용, `getValue()`, `getOrDefault()`로 안전하게 값 가져오기
- **반복문**: 키-값 쌍 순회, 키만 순회
- **클래스 인스턴스**: 맵에 인스턴스 저장 가능하지만 키 타입은 주의해야 해요 (추후 설명 예정)

이제 맵에 대해 좀 더 친숙해졌기를 바라요! 연습 문제를 풀어보면서 더 깊게 이해해보세요. 자세한 예제와 풀이는 [AtomicKotlin 웹사이트](www.AtomicKotlin.com)에서 확인하실 수 있어요!

궁금한 점이 있으면 언제든지 물어봐주세요! 😊