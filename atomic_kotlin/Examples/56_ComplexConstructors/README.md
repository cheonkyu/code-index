# 56. 복잡한 생성자 (Complex Constructors)

안녕하세요! Kotlin 프로그래밍을 처음 배우는 분들을 위해 오늘은 복잡한 생성자에 대해 쉽게 설명해 드리겠습니다. 생성자는 클래스의 인스턴스를 생성할 때 필요한 초기 설정을 담당하는 특별한 함수라고 생각하면 돼요. 이번 챕터에서는 기본 생성자부터 좀 더 복잡한 생성자까지 살펴보겠습니다.

## 기본 생성자 이해하기

### 간단한 생성자 예시
기본 생성자는 주로 객체를 초기화하는 데 사용됩니다. Kotlin에서는 간단한 생성자를 작성할 때 별도의 코드를 직접 작성하지 않아도 되요. 대신 `val` 또는 `var` 키워드를 사용해 객체의 속성을 설정하면 됩니다.

```kotlin
// Alien 클래스 예시
package complexconstructors
import atomictest.eq // 테스트 라이브러리 가정

class Alien(val name: String) {  // 생성자 매개변수 'name'을 정의
    fun main() {
        val alien = Alien("Pencilvester")  // 객체 생성
        alien.name eq "Pencilvester"  // 이름이 올바르게 초기화되었는지 확인
    }
}
```

**핵심 개념:**
- `val name: String`: 객체의 `name` 속성을 초기화합니다.
- Kotlin은 이 매개변수를 기반으로 객체를 자동으로 초기화해줍니다.

## 생성자 내 `init` 블록 이해하기

생성자가 좀 더 복잡한 작업을 해야 할 때는 `init` 블록을 사용합니다. `init` 블록 내의 코드는 객체가 생성될 때 실행됩니다.

```kotlin
// Message 클래스 예시
package complexconstructors
import atomictest.eq

class Message(text: String) {
    private val content: String  // 속성 초기화 전에는 값이 없음

    init {  // 객체 생성 시 실행되는 코드 블록
        val counter = 0
        counter += 10
        content = "[$counter] $text"  // 카운터 값을 포함한 내용 초기화
    }

    override fun toString() = content  // 객체의 문자열 표현을 반환
}

fun main() {
    val m1 = Message("Big ba-da boom!")
    m1 eq "[10] Big ba-da boom!"  // 출력 확인
    val m2 = Message("Bzzzzt!")
    m2 eq "[20] Bzzzzt!"  // 출력 확인
}
```

**핵심 개념:**
- `init` 블록 내에서 객체의 초기 설정을 직접 제어할 수 있어요.
- `var` 또는 `val` 없이도 매개변수를 사용할 수 있지만, 반드시 초기화해야 합니다.
- `content`는 `init` 블록 내에서만 초기화되므로 정의 시점에는 초기화되지 않아요.

## 여러 생성자 (Overloaded Constructors)

한 클래스에 여러 가지 방법으로 객체를 생성할 수 있도록 여러 생성자를 정의할 수 있어요. 이를 **중첩 생성자**라고 부릅니다.

### 중첩 생성자 예시

```kotlin
// WithSecondary 클래스 예시
package secondaryconstructors
import atomictest.*

class WithSecondary(i: Int) {
    init {
        trace("Primary: $i")  // 기본 생성자 호출 시 실행
    }

    constructor(c: Char) : this(c - 'A') {  // 문자 생성자 호출
        trace("Secondary: '$c'")
    }

    constructor(s: String) : this(s.first()) {  // 문자열 생성자 호출
        trace("Secondary: \"$s\"")
    }

    // 주의: 기본 생성자 호출이 없는 생성자는 컴파일 오류 발생
    // constructor(f: Float) { trace("Secondary: $f") }  // 주석 처리
}

fun main() {
    fun sep() = trace("-".repeat(10))  // 구분선 출력 함수

    WithSecondary(1)  // 기본 생성자 호출
    sep()
    WithSecondary('D')  // 문자 생성자 호출
    sep()
    WithSecondary("Last Constructor")  // 문자열 생성자 호출
}
```

**핵심 개념:**
- **기본 생성자**: 클래스 정의 시 자동으로 생성되는 생성자입니다.
- **중첩 생성자**: `constructor()` 키워드를 사용해 여러 방법으로 객체를 생성할 수 있어요.
- `this()`를 사용해 다른 생성자를 호출할 때는 반드시 해당 생성자가 먼저 호출되어야 합니다. 호출 순서가 중요해요!

---

이렇게 복잡한 생성자를 이해하면 Kotlin 객체 생성에 있어서 더 유연하게 접근할 수 있어요. 연습을 통해 더 많은 예제를 접하고 직접 코드를 작성해보세요! 더 궁금한 점이 있으면 언제든지 물어보세요!