describe('Register', () => {
  it('Registration works', () => {
    cy.visit('http://134.209.135.45/');
    cy.get('.Register .Username').click();
    cy.get('.Register .Username').type('tester');
    cy.get('.Input:nth-child(3) > .Email').click();
    cy.get('.Input:nth-child(3) > .Email').type('tester@gmail.com');
    cy.get('.Input:nth-child(4) > .Password').click();
    cy.get('.Input:nth-child(4) > .Password').type('tester');
    cy.get('.Input:nth-child(5) > .Password').click();
    cy.get('.Input:nth-child(5) > .Password').type('tester');
    cy.get('p:nth-child(6) > button').click();
    cy.get('.LogIn').click();
    cy.get('.LogIn .Username').click();
    cy.get('.LogIn .Username').type('tester');
    cy.get('.Input:nth-child(3) > .Password').click();
    cy.get('.Input:nth-child(3) > .Password').type('tester');
    cy.get('p:nth-child(4) > button').click();
    cy.url().should('contains', 'http://134.209.135.45/');
  })
})

//Test