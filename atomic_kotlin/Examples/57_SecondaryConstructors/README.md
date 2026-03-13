# 57. SecondaryConstructors

안녕하세요! 오늘은 코틀린 프로그래밍에서 좀 더 유연하게 객체를 생성하는 방법인 **Secondary Constructors**에 대해 배워볼게요. 초보자분들껜 조금 헷갈릴 수 있지만, 차근차근 따라 해보면 어렵지 않아요!

## 무엇이 Secondary Constructors인가요?

기본적으로 클래스 객체를 만들 때 여러 가지 방법으로 초기화하고 싶을 때 Secondary Constructors를 사용해요. 쉽게 말해, **동일한 클래스의 객체를 여러 가지 방식으로 생성할 수 있게 해주는 추가적인 생성자**라고 생각하면 돼요.

### Primary vs Secondary Constructors

- **Primary Constructor**: 클래스 이름 바로 다음에 오는 기본 생성자예요. 객체 초기화의 기본적인 부분을 담당해요.
  - 예시 코드:
    ```kotlin
    class WithSecondary(i: Int) {
        init {
            println("Primary: $i")  // 초기화 코드
        }
        
        // Secondary Constructors
        constructor(c: Char) : this(c - 'A') {  // 'this'를 사용해 Primary Constructor 호출
            println("Secondary: '$c'")
        }
        
        constructor(s: String) : this(s.first()) {  // 또 다른 Secondary 호출
            println("Secondary: \"$s\"")
        }
    }
    ```

- **Secondary Constructors**: Primary Constructor 외에 추가로 필요한 생성자가 필요할 때 사용해요. `this()` 키워드를 통해 Primary Constructor를 호출해 기본 초기화를 이어받아요.

### 어떻게 사용하나요?

1. **Primary Constructor 호출**: Secondary Constructor 내부에서 `this()`를 호출하면서 Primary Constructor를 먼저 실행시켜야 해요. 이렇게 하면 기본 초기화가 먼저 이루어져요.
   
2. **추가 초기화**: Primary Constructor에서 설정되지 않은 부분을 Secondary Constructor에서 추가로 초기화해요.

#### 예제 코드 분석

```kotlin
fun main() {
    val item1 = WithSecondary(1)  // Primary Constructor 호출
    println("---------")
    val item2 = WithSecondary('D')  // 첫 번째 Secondary Constructor 호출
    println("---------")
    val item3 = WithSecondary("Last Constructor")  // 두 번째 Secondary 호출
}
```

- `WithSecondary(1)`: Primary Constructor가 호출되며 출력: `Primary: 1`
- `WithSecondary('D')`: 첫 번째 Secondary Constructor가 호출되며 출력: `Primary: ${('D' - 'A')}`, `Secondary: 'D'`
- `WithSecondary("Last Constructor")`: 두 번째 Secondary Constructor 호출되며 출력: `Primary: ${("Last Constructor".first())}`, `Secondary: "Last Constructor"`

### 주의사항

- **Primary 호출 필수**: 모든 Secondary Constructor는 반드시 Primary Constructor를 호출해야 해요. 그렇지 않으면 컴파일 오류가 발생해요.
- **공통 초기화**: 공통 초기화 로직은 Primary Constructor에 넣는 것이 좋아요. 이렇게 하면 코드 중복을 줄이고 유지보수를 쉽게 할 수 있어요.

## 간단한 예시: `GardenItem` 클래스

```kotlin
class GardenItem(val name: String) {
    var material: Material = Plastic

    // Primary Constructor
    constructor(name: String, material: Material) : this(name) {  // Primary 호출
        this.material = material
    }

    // Secondary Constructor 예시 (필요한 경우에만 사용)
    constructor(material: Material) : this("Strange Thing", material) {  // 주의: 중복 호출 주의
        // body 생략 가능 (필수는 아님)
    }

    override fun toString() = "$material $name"
}

fun main() {
    val item1 = GardenItem("Elf")  // material은 기본값 Plastic으로 설정
    println(item1)  // 출력: Plastic Elf

    val item2 = GardenItem("Snowman", Material.Metal)  // material 직접 지정
    println(item2)  // 출력: Metal Snowman

    val item3 = GardenItem(Material.Ceramic)  // name은 기본값 "Strange Thing"으로 설정
    println(item3)  // 출력: Ceramic Strange Thing
}
```

### 핵심 요약

- **Secondary Constructors**는 동일 클래스의 객체를 다양한 방법으로 생성할 수 있게 해줘요.
- **Primary Constructor**는 필수로 호출되어야 하며, 기본 초기화를 담당해요.
- **Secondary Constructor**는 추가적인 초기화 로직을 담당해요.
- **공통 초기화 로직**은 Primary Constructor에 포함시키는 것이 좋습니다.

이해하기 어려웠던 부분이 있으면 언제든지 물어보세요! 연습을 통해 점점 익숙해질 거예요. 함께 성장해봐요! 😊