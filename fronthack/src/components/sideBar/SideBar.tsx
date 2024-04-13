import { useState } from 'react';
import axios from 'axios';
import logo from '../../img/logo.png';
import download from '../../img/download.svg';
import Button from '../button/Button';
import InputChoice from '../inputChoice/InputChoice';
import InputDate from '../inputDate/InputDate';
import InputFile from '../inputFile/InputFile';
import { useNavigate } from 'react-router-dom';
import './style.scss';

type SideBaeProps = {
    setData: React.Dispatch<React.SetStateAction<any>>
};

const SideBar = (props: SideBaeProps): JSX.Element => {
    const [inputDate, setInputDate] = useState<string>('');
    const [file, setFile] = useState<File>();
    const [model, setModel] = useState<string>('');
    const navigate = useNavigate();

    const handleSubmit: React.FormEventHandler<HTMLFormElement> = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        console.log('submit');

        if (inputDate && file && model) {
            navigate('/result');
            // props.setData({
            //     model: model,
            //     date: inputDate,
            //     file: file
            // });

            const formdata = new FormData();
            formdata.append("file", file);

            axios({
                url: `http://127.0.0.1:8000/main?date=${inputDate}`,
                method: "POST",
                data: formdata
            })
                .then((response) => {
                    // console.log(response.data.message);
                    props.setData(response.data.message);
                })
                .catch((error) => {
                    console.log(error);
                });
        }
        else {
            navigate('/warning');
        }
    };

    const handleChangeInput: React.ChangeEventHandler<HTMLInputElement> = (event: React.ChangeEvent<HTMLInputElement>) => {
        setInputDate(event.target.value);
    };

    return (
        <div className="side-bar">
            <div className="logo">
                <img src={logo} alt="Логотип" />
            </div>
            <div className="input-bar">
                <form className='form-data' name='form' onSubmit={handleSubmit} >
                    <div className="choice-model">
                        <div className="choice-model-name">
                            <h3>Выберите модель</h3>
                            {/* <span className="wrapper" >
                                <span className="inner">?</span>
                                <span className="tooltip">
                                    Базовая модель - это базовая модель
                                    Продвинутая модель - это продвинутая модель
                                </span>
                            </span> */}
                        </div>
                        <InputChoice
                            className='input-number'
                            setModel={setModel}
                        />
                    </div>
                    <div className="choice-date">
                        <h3>Введите дату</h3>
                        <InputDate
                            value={inputDate}
                            onChange={handleChangeInput}
                            className='input-number'
                            placeholder='Введите число'
                        />
                    </div>
                    <div className="choice-file">
                        <h3>Загрузите данные</h3>
                        <InputFile
                            text="Загрузить"
                            setFile={setFile}
                        >
                            <img
                                className=""
                                src={download}
                                alt="Загрузить"
                            />
                        </InputFile>
                    </div>
                    <hr />
                    <div className="submit">
                        <Button
                            className="btn-submit"
                            text="Старт"
                        />
                    </div>
                </form>
            </div>
        </div>
    );
};

export default SideBar; 