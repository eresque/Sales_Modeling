import Block from '../../components/block/Block';
import Button from '../../components/button/Button';
import home from '../../img/home.svg';
import { Link } from 'react-router-dom';
import './style.scss'

type ResultPageProps = {
    data: string
}

const ResultPage = (props: ResultPageProps): JSX.Element => {
    return (
        <div className="result-page">
            <h1 className="result-name">Результаты вычислений</h1>
            <div className="results">
                <div className='list-dashboards'>
                    <Block className='dashboard-1'>
                        <h3>{props.data}</h3>
                    </Block>
                </div>
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