import './styles/App.scss';
import SideBar from './components/sideBar/SideBar';
import HomePage from './pages/homePage/HomePage';
import ResultPage from './pages/resultPage/ResultPage';
import { Routes, Route } from 'react-router-dom';
import { useState } from 'react';

const App = () => {

    type objData = {
        model: string;
        date: string;
        file: File
    }

    const [data, setData] = useState<objData>();
    console.log(data)

    const fetchData2 = 'Дашборд'

    return (
        <>
            <div className="grad-background"/>
            <SideBar setData={setData} />
            <Routes>
                <Route path='/' element={<HomePage />}/>
                <Route path='/result' element={<ResultPage data={ data ? fetchData2 : 'Заполните все поля ввода' }/>}/>
            </Routes>
        </>
    )
}

export default App;
