//These tests allow to see whether the APIs are functionaing correctly

describe('Login', () => {
  it('Login works', () => {
    cy.visit('http://134.209.135.45/');
    cy.get('.link:nth-child(3)').click();
    cy.get('.Username').click();
    cy.get('.Username').type('tester');
    cy.get('.Password').click();
    cy.get('.Password').type('tester');
    cy.get('button').click();
    cy.url().should('contains', 'http://134.209.135.45/');
    cy.get('.link:nth-child(5)').click();
  })
})


describe('View Communities', () => {
  it('View Communities works', () => {
    cy.visit('http://134.209.135.45/');
    cy.get('.link:nth-child(2)').click();
    cy.url().should('contains', 'http://134.209.135.45/communities');
  })
})

describe('View Specific Community', () => {
  it('View Specific Community works', () => {
    cy.visit('http://134.209.135.45/');
    cy.get('.link:nth-child(2)').click();
    cy.url().should('contains', 'http://134.209.135.45/communities');
    cy.get('button').click();
    cy.wait(500);
    cy.url().should('contains', 'http://134.209.135.45/community?c=TestCommunity');
  })
})





