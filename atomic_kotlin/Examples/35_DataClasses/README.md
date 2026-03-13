# 35. DataClasses

안녕하세요! 코틀린 초보자 여러분, 오늘은 코틀린에서 데이터 클래스(Data Classes)에 대해 배워볼게요. 데이터 클래스는 코드를 간결하고 깔끔하게 만들어주는 강력한 도구랍니다. 특히 데이터를 주로 저장하는 클래스를 작성할 때 정말 유용해요. 이제부터 단계별로 이해하기 쉽게 설명해드릴게요.

## 데이터 클래스의 필요성

코틀린은 반복적인 코드 작성을 줄여줍니다. 하지만 단순히 데이터를 저장하는 클래스를 만들 때는 여전히 많은 코드가 필요했어요. 데이터 클래스는 이런 문제를 해결해주는데요, **`data` 키워드**를 사용해 선언하면 코틀린이 자동으로 몇 가지 유용한 기능을 추가해줘요. 주요 기능들은 다음과 같아요:

1. **읽기 쉬운 객체 표현**: 객체의 속성 값을 쉽게 읽을 수 있는 형식으로 출력해줍니다.
2. **기본적인 동등성 비교**: 객체의 속성 값을 기반으로 자동으로 동등성 비교를 해줍니다.
3. **복사 기능**: 현재 객체의 데이터를 기반으로 새로운 객체를 쉽게 생성할 수 있어요.
4. **해시 기능**: `HashMap`이나 `HashSet`에서 사용할 수 있는 적절한 해시 함수를 자동 생성해줘요.

### 예제 코드 살펴보기

#### 1. 기본 데이터 클래스 예제

```kotlin
// 패키지 데이터 클래스 예제 파일: dataclasses/Simple.kt
package dataclasses

import atomictest.eq  // 테스트 라이브러리 가정

// 데이터 클래스 선언
data class Simple(
    val arg1: String,    // arg1은 읽기 전용 필드
    var arg2: Int        // arg2는 변경 가능한 필드
)

fun main() {
    val s1 = Simple("Hi", 29)
    val s2 = Simple("Hi", 29)
    
    // 데이터 클래스 객체 출력 예시 (자동 생성된 형식)
    println(s1)  // 출력 예시: Simple(arg1=Hi, arg2=29)
    
    // 동등성 비교 자동 생성
    println(s1 eq s2)  // 출력 예시: true
}
```

**설명**:
- `Simple` 클래스는 `data` 키워드로 선언되었어요.
- `arg1`은 읽기 전용(`val`)이고, `arg2`는 변경 가능(`var`)이에요.
- 객체 `s1`과 `s2`가 동일한 값으로 생성되었기 때문에 자동으로 동등성 비교가 이루어져 `true`를 출력해요.

#### 2. 동등성 비교의 중요성

```kotlin
// 패키지 데이터 클래스 예제 파일: dataclasses/DataClasses.kt
package dataclasses

import atomictest.*

// 일반 클래스 예시
class Person(val name: String)

// 데이터 클래스 예시
data class Contact(
    val name: String,
    val number: String
)

fun main() {
    // 일반 클래스의 동등성 비교 (자동 생성되지 않음)
    println(Person("Cleo") neq Person("Cleo"))  // 출력 예시: false (일반 객체는 참조 비교)
    
    // 데이터 클래스의 동등성 비교 자동 생성
    println(Contact("Miffy", "1-234-567890") eq Contact("Miffy", "1-234-567890"))  // 출력 예시: true
}
```

**설명**:
- `Person` 클래스는 `data` 키워드 없이 일반 클래스로 선언되었어요. 따라서 객체는 참조에 따라 동등성을 비교해요.
- 반면 `Contact` 클래스는 데이터 클래스로 선언되었기 때문에 속성 값을 기반으로 자동으로 동등성 비교가 이루어져 `true`를 반환해요.

#### 3. 복사 기능 (`copy`)

```kotlin
// 패키지 데이터 클래스 예제 파일: dataclasses/CopyDataClass.kt
package dataclasses
import atomictest.eq

data class DetailedContact(
    val name: String,
    val surname: String,
    val number: String,
    val address: String
)

fun main() {
    val contact = DetailedContact(
        "Miffy",
        "Miller",
        "1-234-567890",
        "1600 Amphitheatre Parkway"
    )
    
    // 특정 속성만 변경한 새로운 객체 생성
    val newContact = contact.copy(
        number = "098-765-4321",
        address = "Brandschenkestrasse 110"
    )
    
    println(newContact eq DetailedContact(
        "Miffy",
        "Miller",
        "098-765-4321",
        "Brandschenkestrasse 110"
    ))  // 출력 예시: true
}
```

**설명**:
- `copy` 메서드를 사용하면 특정 속성만 변경하면서 새로운 객체를 쉽게 생성할 수 있어요.
- `copy` 메서드의 매개변수는 원래 객체의 생성자 매개변수와 동일해야 해요.

#### 4. 해시 함수 생성

```kotlin
// 패키지 데이터 클래스 예제 파일: dataclasses/HashCode.kt
package dataclasses
import atomictest.eq

data class Key(val name: String, val id: Int)

fun main() {
    val korvo: Key = Key("Korvo", 19)
    println(korvo.hashCode() eq -2041757108)  // 해시 코드 출력 예시
    
    val map = HashMap<Key, String>()
    map[korvo] = "Alien"
    println(map[korvo] eq "Alien")  // 출력 예시: true
    
    val set = HashSet<Key>()
    set.add(korvo)
    println(set.contains(korvo) eq true)  // 출력 예시: true
}
```

**설명**:
- 데이터 클래스는 자동으로 적절한 해시 함수를 생성해 `HashMap`이나 `HashSet`에서 사용할 수 있게 해줘요.
- 이렇게 하면 복잡한 해시 함수를 직접 구현할 필요가 없어져요.

## 핵심 요약

- **데이터 클래스 선언**: `data class` 키워드로 선언해요.
- **필드 타입**: `val`은 읽기 전용, `var`은 변경 가능이에요.
- **자동 생성 기능**:
  - **동등성 비교**: 객체의 속성 값을 기반으로 자동 비교
  - **복사 함수**: `copy()` 메서드로 객체 복제 및 일부 속성 변경 가능
  - **해시 함수**: `HashMap`과 `HashSet`에서 사용 가능

이렇게 데이터 클래스를 사용하면 코드가 훨씬 간결해지고 유지보수가 쉬워져요. 코틀린의 데이터 클래스는 개발자의 시간을 절약하면서도 더 안정적이고 읽기 쉬운 코드를 작성할 수 있게 도와줘요. 연습해보면서 더 익숙해지는 게 좋을 것 같아요!

### 연습 문제

1. 데이터 클래스를 이용해 `Student` 클래스를 작성해보세요. 학생의 이름, 학번, 성적 평균을 저장하도록 하세요.
2. `Student` 클래스의 객체를 생성하고, `copy` 메서드를 사용해 학번만 변경한 새로운 객체를 만들어보세요.
3. `Student` 객체를 `HashMap`에 저장해보세요.

궁금한 점이 있으면 언제든지 물어보세요! 함께 배워가요!