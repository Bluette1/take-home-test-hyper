import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import uuid from 'react-uuid';
import registerPets from '../actions/pet';
import PetService from '../services/pet.service'
import Pet from '../components/PetItem';

const Home = () => {
  const [errDisplay, setErrDisplay] = useState('');
  const dispatch = useDispatch();
  const pets = useSelector((state) => state.pet);

  useEffect(async () => {
    try {

      PetService.getPets()
        .then((response) => {
          dispatch(registerPets(response.data));
        })
        .catch((error) => {
          const errorContent = (error.response && error.response.data)
          || error.message
          || error.toString();
          setErrDisplay(JSON.stringify(errorContent));
        });
    } catch (error) {
      const errorContent = (error.response && error.response.data)
      || error.message
      || error.toString();
      setErrDisplay(JSON.stringify(errorContent));
    }
  }, []);

  if (errDisplay !== '') {
    console.log(errDisplay);
    return null;
  }

  return (
    <div className="container row d-flex">
      <p>Home</p>
      <div className="">
        {pets && pets.length > 0 ? (
          <div className="row d-flex">
            {' '}
            {pets.map((pet) => (
              <Pet
                key={`pet-${uuid()}`}
                pet={pet}
              />
            ))}
          </div>
        ) : null}
      </div>
    </div>
  );
};

export default Home;