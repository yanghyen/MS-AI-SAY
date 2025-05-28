import { useSearchParams } from 'react-router-dom';

const MyP5 = () => {
    const [student, setStudent] = useSearchParams();  // 요청파라미터 활용
  return (
    <>
        <div>MyP5</div>
        <div>{student.get("name")} - {student.get("age")}</div>
    </>
  )
}

export default MyP5