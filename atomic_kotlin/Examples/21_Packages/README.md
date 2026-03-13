# 21. Packages

안녕하세요! 코틀린 프로그래밍을 처음 배우시는 여러분을 위해 패키지에 대해 쉽게 설명해드릴게요. 코틀린에서 패키지는 코드의 논리적인 그룹화와 재사용을 가능하게 하는 핵심 개념이에요. 지금부터 몇 가지 중요한 포인트와 예제를 통해 이해해보도록 할게요.

## DRY 원칙과 패키지의 필요성
먼저, 프로그래밍에서 중요한 원칙인 DRY(Don’t Repeat Yourself)를 기억해보세요. 동일한 코드를 여러 번 작성하면 수정이나 개선을 할 때마다 유지보수 작업이 복잡해져요. 패키지는 이런 문제를 해결해줘요. 필요한 코드를 다른 파일에서 재사용할 수 있게 해줘요.

### 코드 예시: 패키지 임포트하기
```kotlin
// 수학 상수와 함수를 import하는 예시
import kotlin.math.PI       // 원주율 상수
import kotlin.math.cos      // 코사인 함수

fun main() {
    println(PI)              // 원주율 출력
    println(cos(PI))         // 코사인 값 출력 (원주율 대입)
    println(cos(2 * PI))     // 2 * 원주율 대입 후 코사인 값 출력
}
/* 출력 결과:
3.141592653589793
-1.0
1.0
*/
```

### 이름 충돌 해결하기: `as` 키워드 사용
다른 라이브러리에서 동일한 이름의 함수나 클래스가 있을 때 `as` 키워드를 사용하면 이름을 바꿔 사용할 수 있어요.

```kotlin
// 이름 변경 예시
import kotlin.math.PI as circleRatio  // 원주율 이름 변경
import kotlin.math.cos as cosine      // 코사인 함수 이름 변경

fun main() {
    println(circleRatio)             // 변경된 이름으로 출력
    println(cosine(circleRatio))     // 변경된 이름으로 함수 호출
    println(cosine(2 * circleRatio)) // 변경된 이름으로 호출
}
/* 출력 결과:
3.141592653589793
-1.0
1.0
*/
```

### 완전 명시적 임포트
전체 패키지를 명시적으로 불러와서 사용할 수도 있어요. 이렇게 하면 어떤 요소가 어디서 왔는지 명확해져요.

```kotlin
// 완전 명시적 임포트 예시
fun main() {
    println(kotlin.math.PI)           // 명시적으로 패키지 이름을 붙임
    println(kotlin.math.cos(kotlin.math.PI)) // 명시적으로 패키지 이름 붙임
    println(kotlin.math.cos(2 * kotlin.math.PI)) // 명시적으로 패키지 이름 붙임
}
/* 출력 결과:
3.141592653589793
-1.0
1.0
*/
```

### 모든 요소 임포트하기
패키지의 모든 요소를 임포트하려면 `*`를 사용해요. 하지만 주의할 점은 이 방법은 코드의 가독성을 약간 떨어뜨릴 수 있어요.

```kotlin
// 모든 요소 임포트 예시
import kotlin.math.*

fun main() {
    println(E)                      // 상수 E 출력
    println(E.roundToInt())         // 반올림 후 정수 출력
    println(E.toInt())              // 정수로 변환 후 출력
}
/* 출력 결과:
2.718281828459045
3
2
*/
```

## 패키지 생성하기
자신의 코드를 재사용하려면 패키지를 만들어보세요. 패키지는 코드를 구조화하고 관리하는 데 도움이 돼요.

### 패키지 생성 예시
```kotlin
// 패키지 생성 예시
package pythagorean  // 패키지 이름은 소문자로 작성하는 것이 관례

import kotlin.math.sqrt  // 필요한 함수 임포트

class RightTriangle(  // 클래스 정의
    val a: Double,     // 속성 정의
    val b: Double
) {
    fun hypotenuse() = sqrt(a * a + b * b) // 피타고라스 정리 적용
    fun area() = a * b / 2                    // 넓이 계산
}
```

### 패키지 사용 예시
자신이 만든 패키지를 다른 파일에서 사용해볼게요.

```kotlin
// 패키지 사용 예시
import pythagorean.RightTriangle  // 패키지와 클래스 임포트

fun main() {
    val rt = RightTriangle(3.0, 4.0)  // RightTriangle 객체 생성
    println(rt.hypotenuse())           // 빗변 길이 출력
    println(rt.area())                 // 넓이 출력
}
/* 출력 결과:
5.0
6.0
*/
```

### 주요 핵심 요약
- **패키지**: 코드를 논리적으로 그룹화하고 재사용 가능하게 만드는 방법입니다.
- **임포트**: 필요한 코드를 다른 파일에서 불러와서 사용합니다. `import` 키워드를 사용해요.
- **`as` 키워드**: 이름 충돌을 해결하거나 더 간결한 이름으로 변경할 때 사용해요.
- **패키지 생성**: `package` 문을 사용해 자신의 코드를 관리해요. 파일 이름과 디렉토리 이름을 일치시키는 것이 관례에요.

이제 패키지에 대한 기본 개념을 이해하셨길 바라요! 연습을 통해 더 익숙해질 수 있을 거예요. 질문이 있으면 언제든지 물어봐주세요! 😊

### 추가 학습 자료
- [AtomicKotlin 공식 웹사이트](www.AtomicKotlin.com)에서 연습 문제와 해결책을 확인해보세요!