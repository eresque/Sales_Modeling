import Block from '../../components/block/Block';
import './style.scss';

const HomePage = (): JSX.Element => {
    return (
        <div className="home-page">
            <div className="home-name">
                <h1 className="hello">Добро пожаловать</h1>
                <h6 className="emoji">☀️</h6>
            </div>
            <div className="guide">
                <h3 className="question-1">Как пользоваться приложением?</h3>
                <div className='list-steps'>
                    <Block className='step-1'>
                        <h2>Шаг 1</h2>
                        <h3>Выберите модель</h3>
                    </Block>
                    <Block className='step-2'>
                        <h2>Шаг 2</h2>
                        <h3>Введите дату</h3>
                    </Block>
                    <Block className='step-3'>
                        <h2>Шаг 3</h2>
                        <h3>Нажмите на "Старт"</h3>
                    </Block>
                </div>
            </div>
            {/* <div className="explanation-model">
                <h3 className="question-2">Чем отличаются модели друг от друга?</h3>
                <div className='list-models'>
                    <Block className='base-model'>
                        <h3>Базовая модель</h3>
                    </Block>
                    <Block className='super-model'>
                        <h3>Продвинутая модель</h3>
                    </Block>
                </div>
            </div> */}
        </div>
    );
};

export default HomePage; 