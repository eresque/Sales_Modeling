import './styles/App.scss';
import SideBar from './components/sideBar/SideBar';
import HomePage from './pages/homePage/HomePage';
import ResultPage from './pages/resultPage/ResultPage';
import WarningPage from './pages/warningPage/WarningPage';
import { Routes, Route } from 'react-router-dom';
import { useState } from 'react';

const App = () => {

    const [data, setData] = useState<object>();
    console.log(data)

    return (
        <>
            <div className="grad-background"/>
            <SideBar setData={setData} />
            <Routes>
                <Route 
                    path='/' 
                    element={<HomePage />}
                />
                { data == undefined || data == null ?
                    <Route 
                        path='/warning' 
                        element={<WarningPage />}
                    /> :
                    <Route 
                        path='/result' 
                        element={<ResultPage />}
                    />
                }
            </Routes>
        </>
    )
}

export default App;
