import Block from '../../components/block/Block';
import Button from '../../components/button/Button';
import png from '../../img/logo.png';
import download from '../../img/download.svg';
import home from '../../img/home.svg';
import { Link } from 'react-router-dom';
import { useState } from 'react';
import './style.scss'

type ResultPageProps = {
    data: Array<string>
}

const ResultPage = (props: ResultPageProps): JSX.Element => {
    const [_, setValue] = useState(0);

    setTimeout(() => {
        // useForceUpdate();
        console.log(props.data);
        setValue(100);
        // ResultPage.forceUpdate();
    }, 2000);

    return (
        <div className="result-page">
            <h1 className="result-name">Результаты вычислений</h1>
            <div className="results">
                <Block className='block-res'>
                    <div className='list-dashboards'>
                        <Block className='dashboard-1'>
                            <img src={props.data[0]} alt="" />
                        </Block>
                        <Block className='dashboard-2'>
                            <img src={props.data[2]} alt="" />
                        </Block>
                    </div>
                    <a
                        className="download-results"
                        href={png}
                        download="Результаты вычислений"
                        target="_blank"
                        rel="noreferrer"
                    >
                        <img className="icon-download" src={download} alt="Скачать результаты" />
                        <h4 className="message-download">Скачать .zip</h4>
                    </a>
                </Block>
            </div>
            <div className="help">
                <div className="help-text">
                    <h2 className="help-message">Забыли, как пользоваться? Жми сюда</h2>
                    <h6 className="emoji-right">👉</h6>
                    <h6 className="emoji-down">👇</h6>
                </div>
                <div className="home">
                    <Link to="/" className="link">
                        <Button
                            className="btn-home"
                            text="Домой">
                            <img
                                src={home}
                                alt="Дом"
                            />
                        </Button>
                    </Link>
                </div>
            </div>
        </div>
    );
};

export default ResultPage; 